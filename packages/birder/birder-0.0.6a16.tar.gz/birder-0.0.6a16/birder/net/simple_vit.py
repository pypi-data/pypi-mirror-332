"""
Simple ViT, adapted from
https://github.com/pytorch/vision/blob/main/torchvision/models/vision_transformer.py
and
https://github.com/lucidrains/vit-pytorch/blob/main/vit_pytorch/simple_vit.py

Paper "Better plain ViT baselines for ImageNet-1k",
https://arxiv.org/abs/2205.01580
"""

# Reference license: BSD 3-Clause and MIT

import math
from functools import partial
from typing import Any
from typing import Optional

import torch
from torch import nn

from birder.model_registry import registry
from birder.net.base import PreTrainEncoder
from birder.net.base import pos_embedding_sin_cos_2d
from birder.net.vit import Encoder
from birder.net.vit import EncoderBlock
from birder.net.vit import PatchEmbed


# pylint: disable=invalid-name
class Simple_ViT(PreTrainEncoder):
    block_group_regex = r"encoder\.block\.(\d+)"

    def __init__(
        self,
        input_channels: int,
        num_classes: int,
        *,
        net_param: Optional[float] = None,
        config: Optional[dict[str, Any]] = None,
        size: Optional[tuple[int, int]] = None,
    ) -> None:
        super().__init__(input_channels, num_classes, net_param=net_param, config=config, size=size)
        assert self.net_param is None, "net-param not supported"
        assert self.config is not None, "must set config"

        image_size = self.size
        drop_path_rate = 0.0
        patch_size: int = self.config["patch_size"]
        num_layers: int = self.config["num_layers"]
        num_heads: int = self.config["num_heads"]
        hidden_dim: int = self.config["hidden_dim"]
        mlp_dim: int = self.config["mlp_dim"]

        torch._assert(image_size[0] % patch_size == 0, "Input shape indivisible by patch size!")
        torch._assert(image_size[1] % patch_size == 0, "Input shape indivisible by patch size!")
        self.patch_size = patch_size
        self.num_layers = num_layers
        self.hidden_dim = hidden_dim
        self.mlp_dim = mlp_dim
        self.num_special_tokens = 0
        self.num_classes = num_classes
        dpr = [x.item() for x in torch.linspace(0, drop_path_rate, num_layers)]  # Stochastic depth decay rule

        self.conv_proj = nn.Conv2d(
            self.input_channels,
            hidden_dim,
            kernel_size=(patch_size, patch_size),
            stride=(patch_size, patch_size),
            padding=(0, 0),
            bias=True,
        )
        self.patch_embed = PatchEmbed()

        # Add positional embedding
        pos_embedding = pos_embedding_sin_cos_2d(
            h=image_size[0] // patch_size,
            w=image_size[1] // patch_size,
            dim=hidden_dim,
            num_special_tokens=self.num_special_tokens,
        )
        self.pos_embedding = nn.Parameter(pos_embedding, requires_grad=False)

        self.encoder = Encoder(num_layers, num_heads, hidden_dim, mlp_dim, dropout=0.0, attention_dropout=0.0, dpr=dpr)
        self.norm = nn.LayerNorm(hidden_dim, eps=1e-6)
        self.features = nn.Sequential(
            nn.AdaptiveAvgPool1d(output_size=1),
            nn.Flatten(1),
        )

        self.embedding_size = hidden_dim
        self.classifier = self.create_classifier()

        self.encoding_size = hidden_dim * (image_size[0] // patch_size) * (image_size[1] // patch_size)
        self.decoder_block = partial(
            EncoderBlock,
            16,
            mlp_dim=None,
            dropout=0,
            attention_dropout=0,
            drop_path=0,
            activation_layer=nn.GELU,
        )

        # Weight initialization
        if isinstance(self.conv_proj, nn.Conv2d):
            # Init the patchify stem
            fan_in = self.conv_proj.in_channels * self.conv_proj.kernel_size[0] * self.conv_proj.kernel_size[1]
            nn.init.trunc_normal_(self.conv_proj.weight, std=math.sqrt(1 / fan_in))
            if self.conv_proj.bias is not None:
                nn.init.zeros_(self.conv_proj.bias)

        if isinstance(self.classifier, nn.Linear):
            nn.init.zeros_(self.classifier.weight)
            nn.init.zeros_(self.classifier.bias)

    def masked_encoding(
        self,
        x: torch.Tensor,
        mask_ratio: float,
        kept_mask_ratio: Optional[float] = None,
        mask_token: Optional[torch.Tensor] = None,
        return_all_features: bool = False,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        if kept_mask_ratio is None:
            kept_mask_ratio = mask_ratio

        # Reshape and permute the input tensor
        x = self.conv_proj(x)
        x = self.patch_embed(x)

        # Add pos embedding
        x = x + self.pos_embedding

        # Masking: length -> length * mask_ratio
        # Perform per-sample random masking by per-sample shuffling.
        # Per-sample shuffling is done by argsort random noise.
        (N, L, D) = x.shape  # batch, length, dim
        len_keep = int(L * (1 - mask_ratio))
        len_masked = int(L * (mask_ratio - kept_mask_ratio))

        noise = torch.rand(N, L, device=x.device)  # Noise in [0, 1]

        # Sort noise for each sample
        ids_shuffle = torch.argsort(noise, dim=1)  # Ascend: small is keep, large is remove
        ids_restore = torch.argsort(ids_shuffle, dim=1)

        # Keep the first subset
        ids_keep = ids_shuffle[:, :len_keep]
        x_masked = torch.gather(x, dim=1, index=ids_keep.unsqueeze(-1).repeat(1, 1, D))

        # Generate the binary mask: 0 is keep, 1 is remove
        mask = torch.ones([N, L], device=x.device)
        mask[:, : len_keep + len_masked] = 0

        # Un-shuffle to get the binary mask
        mask = torch.gather(mask, dim=1, index=ids_restore)

        x = x_masked

        # Apply transformer
        if return_all_features is True:
            xs = self.encoder.forward_features(x)
            xs[-1] = self.norm(xs[-1])
            x = torch.stack(xs, dim=-1)
        else:
            x = self.encoder(x)
            x = self.norm(x)

        return (x, mask, ids_restore)

    def embedding(self, x: torch.Tensor) -> torch.Tensor:
        x = self.conv_proj(x)
        x = self.patch_embed(x)
        x = x + self.pos_embedding
        x = self.encoder(x)
        x = self.norm(x)
        x = x.permute(0, 2, 1)
        return self.features(x)

    def adjust_size(self, new_size: tuple[int, int]) -> None:
        if new_size == self.size:
            return

        super().adjust_size(new_size)

        # Sort out sizes
        pos_embedding = pos_embedding_sin_cos_2d(
            h=new_size[0] // self.patch_size,
            w=new_size[1] // self.patch_size,
            dim=self.hidden_dim,
            num_special_tokens=self.num_special_tokens,
        )
        self.pos_embedding = nn.Parameter(pos_embedding, requires_grad=False)


registry.register_alias(
    "simple_vit_b32",
    Simple_ViT,
    config={"patch_size": 32, "num_layers": 12, "num_heads": 12, "hidden_dim": 768, "mlp_dim": 3072},
)
registry.register_alias(
    "simple_vit_b16",
    Simple_ViT,
    config={"patch_size": 16, "num_layers": 12, "num_heads": 12, "hidden_dim": 768, "mlp_dim": 3072},
)
registry.register_alias(
    "simple_vit_l32",
    Simple_ViT,
    config={"patch_size": 32, "num_layers": 24, "num_heads": 16, "hidden_dim": 1024, "mlp_dim": 4096},
)
registry.register_alias(
    "simple_vit_l16",
    Simple_ViT,
    config={"patch_size": 16, "num_layers": 24, "num_heads": 16, "hidden_dim": 1024, "mlp_dim": 4096},
)
registry.register_alias(
    "simple_vit_h14",
    Simple_ViT,
    config={"patch_size": 14, "num_layers": 32, "num_heads": 16, "hidden_dim": 1280, "mlp_dim": 5120},
)
