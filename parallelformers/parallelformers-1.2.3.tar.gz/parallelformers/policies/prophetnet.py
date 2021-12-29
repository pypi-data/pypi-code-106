# Copyright 2021 TUNiB inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from transformers.models.prophetnet.modeling_prophetnet import (
    ProphetNetDecoderLayer,
    ProphetNetEncoderLayer,
)

from parallelformers.policies.base import Layer, Policy
from parallelformers.transformers.modeling_prophetnet import (
    ProphetNetAttention_,
)
from parallelformers.utils.dist_utils import AllReduceLinear


class ProphetNetEncoderPolicy(Policy):
    @staticmethod
    def replace_arguments(config, world_size):
        return {
            # 1. reduce number of heads
            "self_attn.hidden_size": config.hidden_size // world_size,
            # 2. reduce number of heads
            "self_attn.num_attn_heads": config.num_encoder_attention_heads
            // world_size,
        }

    @staticmethod
    def replace_modules():
        return {"ProphetNetAttention": ProphetNetAttention_}

    @staticmethod
    def attn_qkv():
        return [
            Layer(
                weight="self_attn.query_proj.weight",
                bias="self_attn.query_proj.bias",
            ),
            Layer(
                weight="self_attn.key_proj.weight",
                bias="self_attn.key_proj.bias",
            ),
            Layer(
                weight="self_attn.value_proj.weight",
                bias="self_attn.value_proj.bias",
            ),
        ]

    @staticmethod
    def attn_out():
        return [
            Layer(
                weight="self_attn.out_proj.weight",
                bias="self_attn.out_proj.bias",
                replace=AllReduceLinear,
            ),
        ]

    @staticmethod
    def mlp_in():
        return [
            Layer(
                weight="feed_forward.intermediate.weight",
                bias="feed_forward.intermediate.bias",
            ),
        ]

    @staticmethod
    def mlp_out():
        return [
            Layer(
                weight="feed_forward.output.weight",
                bias="feed_forward.output.bias",
                replace=AllReduceLinear,
            ),
        ]

    @staticmethod
    def original_layer_class():
        return ProphetNetEncoderLayer


class ProphetNetDecoderPolicy(Policy):
    @staticmethod
    def replace_arguments(config, world_size):
        return {
            # 1. reduce hidden size
            "cross_attn.hidden_size": config.hidden_size // world_size,
            # 2. reduce number of heads
            "cross_attn.num_attn_heads": config.num_decoder_attention_heads
            // world_size,
        }

    @staticmethod
    def replace_modules():
        return {
            "ProphetNetAttention": ProphetNetAttention_,
        }

    @staticmethod
    def attn_qkv():
        return [
            Layer(
                weight="cross_attn.query_proj.weight",
                bias="cross_attn.query_proj.bias",
            ),
            Layer(
                weight="cross_attn.key_proj.weight",
                bias="cross_attn.key_proj.bias",
            ),
            Layer(
                weight="cross_attn.value_proj.weight",
                bias="cross_attn.value_proj.bias",
            ),
        ]

    @staticmethod
    def attn_out():
        return [
            Layer(
                weight="cross_attn.out_proj.weight",
                bias="cross_attn.out_proj.bias",
                replace=AllReduceLinear,
            ),
        ]

    @staticmethod
    def mlp_in():
        return [
            Layer(
                weight="feed_forward.intermediate.weight",
                bias="feed_forward.intermediate.bias",
            ),
        ]

    @staticmethod
    def mlp_out():
        return [
            Layer(
                weight="feed_forward.output.weight",
                bias="feed_forward.output.bias",
                replace=AllReduceLinear,
            ),
        ]

    @staticmethod
    def original_layer_class():
        return ProphetNetDecoderLayer
