from nai_t5 import T5, T5Config
from nai_t5.t5_encoder import T5EncoderStack, T5EncoderLayer
from nai_t5.t5_decoder import T5DecoderStack, T5DecoderLayer
from typing import Optional, OrderedDict, TYPE_CHECKING, Any, Protocol, Literal, Callable, NamedTuple, Sequence
from dataclasses import dataclass, field
from functools import partial
import contextlib
import torch
from torch import FloatTensor, inference_mode
from torch.nn import Linear, Module
from tensorizer import TensorDeserializer, TensorType
import re

if TYPE_CHECKING:
    from tensorizer._tensor_path import _TensorPath
else:
    _TensorPath = Any

@dataclass
class EncScales:
    attn_out_scales: list[float]
    attn_out_scales_cp_hat: list[float]
    ffn_out_scales: list[float]
    ffn_out_scales_cp_hat: list[float]
    ln1_eps_scales: list[float]
    ln2_eps_scales: list[float]
    final_norm_eps_scale: float

@dataclass
class DecScales:
    self_attn_out_scales: list[float]
    self_attn_out_scales_cp_hat: list[float]
    cross_attn_out_scales: list[float]
    cross_attn_out_scales_cp_hat: list[float]
    ffn_out_scales: list[float]
    ffn_out_scales_cp_hat: list[float]
    ln1_eps_scales: list[float]
    ln2_eps_scales: list[float]
    ln3_eps_scales: list[float]
    final_norm_eps_scale: float

def resolve_enc_scales(
    attn_out_scales: Optional[list[float]] = None,
    ffn_out_scales: Optional[list[float]] = None,
) -> EncScales:
    attn_out_scales: FloatTensor = torch.tensor(attn_out_scales, dtype=torch.float32)
    attn_out_scales_cp: FloatTensor = attn_out_scales.cumprod(-1)

    ffn_out_scales: FloatTensor = torch.tensor(ffn_out_scales, dtype=torch.float32)
    ffn_out_scales_cp: FloatTensor = ffn_out_scales.cumprod(-1)

    attn_out_scales_cp_hat = attn_out_scales_cp.clone()
    attn_out_scales_cp_hat[1:].mul_(ffn_out_scales_cp[:-1])

    ffn_out_scales_cp_hat = ffn_out_scales_cp.clone()
    ffn_out_scales_cp_hat.mul_(attn_out_scales_cp)

    ln1_eps_scales = ffn_out_scales_cp_hat.roll(1, dims=-1)
    ln1_eps_scales[0].copy_(1)

    ln2_eps_scales = attn_out_scales_cp_hat

    final_norm_eps_scale = ffn_out_scales_cp_hat[-1].item()

    return EncScales(
        attn_out_scales=attn_out_scales.tolist(),
        attn_out_scales_cp_hat=attn_out_scales_cp_hat.tolist(),
        ffn_out_scales=ffn_out_scales.tolist(),
        ffn_out_scales_cp_hat=ffn_out_scales_cp_hat.tolist(),
        ln1_eps_scales=ln1_eps_scales.tolist(),
        ln2_eps_scales=ln2_eps_scales.tolist(),
        final_norm_eps_scale=final_norm_eps_scale,
    )

def resolve_dec_scales(
    self_attn_out_scales: Optional[list[float]] = None,
    cross_attn_out_scales: Optional[list[float]] = None,
    ffn_out_scales: Optional[list[float]] = None,
) -> DecScales:
    self_attn_out_scales: FloatTensor = torch.tensor(self_attn_out_scales, dtype=torch.float32)
    self_attn_out_scales_cp: FloatTensor = self_attn_out_scales.cumprod(-1)

    cross_attn_out_scales: FloatTensor = torch.tensor(cross_attn_out_scales, dtype=torch.float32)
    cross_attn_out_scales_cp: FloatTensor = cross_attn_out_scales.cumprod(-1)

    ffn_out_scales: FloatTensor = torch.tensor(ffn_out_scales, dtype=torch.float32)
    ffn_out_scales_cp: FloatTensor = ffn_out_scales.cumprod(-1)

    self_attn_out_scales_cp_hat = self_attn_out_scales_cp.clone()
    self_attn_out_scales_cp_hat[1:].mul_(cross_attn_out_scales_cp[:-1])
    self_attn_out_scales_cp_hat[1:].mul_(ffn_out_scales_cp[:-1])

    cross_attn_out_scales_cp_hat = cross_attn_out_scales_cp.clone()
    cross_attn_out_scales_cp_hat.mul_(self_attn_out_scales_cp)
    cross_attn_out_scales_cp_hat[1:].mul_(ffn_out_scales_cp[:-1])

    ffn_out_scales_cp_hat = ffn_out_scales_cp.clone()
    ffn_out_scales_cp_hat.mul_(self_attn_out_scales_cp)
    ffn_out_scales_cp_hat.mul_(cross_attn_out_scales_cp)

    ln1_eps_scales = ffn_out_scales_cp_hat.roll(1, dims=-1)
    ln1_eps_scales[0].copy_(1)

    ln2_eps_scales = self_attn_out_scales_cp_hat

    ln3_eps_scales = cross_attn_out_scales_cp_hat

    final_norm_eps_scale = ffn_out_scales_cp_hat[-1].item()

    return DecScales(
        self_attn_out_scales=self_attn_out_scales.tolist(),
        self_attn_out_scales_cp_hat=self_attn_out_scales_cp_hat.tolist(),
        cross_attn_out_scales=cross_attn_out_scales.tolist(),
        cross_attn_out_scales_cp_hat=cross_attn_out_scales_cp_hat.tolist(),
        ffn_out_scales=ffn_out_scales.tolist(),
        ffn_out_scales_cp_hat=ffn_out_scales_cp_hat.tolist(),
        ln1_eps_scales=ln1_eps_scales.tolist(),
        ln2_eps_scales=ln2_eps_scales.tolist(),
        ln3_eps_scales=ln3_eps_scales.tolist(),
        final_norm_eps_scale=final_norm_eps_scale,
    )

class AcceptFusion(Protocol):
    @staticmethod
    def __call__(attr: str, tensor: FloatTensor) -> None: ...

def fuse_norm_scale(
    w: FloatTensor,
    ln_scale: FloatTensor,
    scale_via_f32 = False,
) -> FloatTensor:
    higher_type: torch.dtype = torch.float32 if scale_via_f32 else torch.promote_types(w.dtype, ln_scale.dtype)
    scale_diag: FloatTensor = torch.eye(
        ln_scale.size(-1),
        device=ln_scale.device,
        dtype=higher_type,
    ) * ln_scale.type(higher_type).unsqueeze(-1)
    matmul_type = torch.float32 if scale_via_f32 else higher_type
    w.copy_(w.type(matmul_type) @ scale_diag.type(matmul_type))

class FusionSpec(NamedTuple):
    norm_weights: str
    linear_weights: Sequence[str]

@dataclass(frozen=True, slots=True)
class FusionTask:
    spec: FusionSpec
    awaiting: set[str]
    norm_fusion_via_f32: bool = False
    weights: dict[str, FloatTensor] = field(init=False, default_factory=dict)
    linears: dict[str, Linear] = field(init=False, default_factory=dict)
    linear_attrs: dict[str, str] = field(init=False, default_factory=dict)

    def accept(self, name: str, module: Module, attr: str, tensor: FloatTensor) -> bool:
        assert name in self.awaiting
        assert name not in self.weights
        self.awaiting.remove(name)
        self.weights[name] = tensor
        if isinstance(module, Linear):
            self.linears[name] = module
            self.linear_attrs[name] = attr
        if self.awaiting:
            return False
        ln_scale: FloatTensor = self.weights[self.spec.norm_weights]
        for name, linear in self.linears.items():
            linear_attr: str = self.linear_attrs[name]
            weight: str = self.weights[name]
            fuse_norm_scale(
                w=weight,
                ln_scale=ln_scale,
                scale_via_f32=self.norm_fusion_via_f32,
            )
            linear.register_parameter(linear_attr, weight)
        return True

class FusingDeserializer(TensorDeserializer):
    def load_with_fusions(
        self,
        m: T5 | T5EncoderStack,
        norm_fusion_via_f32 = False,
        fuse_norm_scales = False,
        enc_attn_out_scales: Optional[list[float]] = None,
        enc_ffn_out_scales: Optional[list[float]] = None,
        dec_self_attn_out_scales: Optional[list[float]] = None,
        dec_cross_attn_out_scales: Optional[list[float]] = None,
        dec_ffn_out_scales: Optional[list[float]] = None,
        verify_hash: Optional[bool] = None,
    ) -> int:
        """
        Load weights into a model, fusing or scaling layers as we go.
        """
        config: T5Config = m.config
        enc_scales: EncScales = resolve_enc_scales(
            enc_attn_out_scales or [1.] * config.num_layers,
            enc_ffn_out_scales or [1.] * config.num_layers,
        )
        dec_scales: DecScales = resolve_dec_scales(
            dec_self_attn_out_scales or [1.] * config.num_layers,
            dec_cross_attn_out_scales or [1.] * config.num_layers,
            dec_ffn_out_scales or [1.] * config.num_layers,
        )

        def receives_residual(obj_path: str, qualifier: Optional[Literal['encoder', 'decoder']] = None) -> bool:
            prefix = f"{qualifier}." if qualifier else ''
            return obj_path == f'{prefix}ln' or obj_path.startswith(f'{prefix}layers.')

        match m:
            case T5():
                receives_enc_residual: Callable[[str], bool] = partial(receives_residual, qualifier='encoder')
                receives_dec_residual: Callable[[str], bool] = partial(receives_residual, qualifier='decoder')
                enc: T5EncoderStack = m.encoder
                dec: T5DecoderStack = m.decoder
            case T5EncoderStack():
                receives_enc_residual: Callable[[str], bool] = receives_residual
                receives_dec_residual: Callable[[str], bool] = lambda _: False
                enc: T5EncoderStack = m
                dec: Optional[T5DecoderStack] = None
            case _:
                raise ValueError(f"Unsupported model type: {type(m)}")
        
        for (
            layer,
            ln1_eps_scale,
            ln2_eps_scale,
            ln1_residual_scale,
            ln2_residual_scale,
        ) in zip(
            enc.layers,
            enc_scales.ln1_eps_scales,
            enc_scales.ln2_eps_scales,
            enc_scales.attn_out_scales,
            enc_scales.ffn_out_scales,
        ):
            layer: T5EncoderLayer
            layer.ln1.eps *= ln1_eps_scale
            layer.ln2.eps *= ln2_eps_scale
            # make residual smaller at the same time as we make a layer output smaller
            layer.ln1.residual_scale = ln1_residual_scale
            layer.ln2.residual_scale = ln2_residual_scale
        enc.ln.eps *= enc_scales.final_norm_eps_scale

        if dec is not None:
            for (
                layer,
                ln1_eps_scale,
                ln2_eps_scale,
                ln3_eps_scale,
                ln1_residual_scale,
                ln2_residual_scale,
                ln3_residual_scale,
            ) in zip(
                dec.layers,
                dec_scales.ln1_eps_scales,
                dec_scales.ln2_eps_scales,
                dec_scales.ln3_eps_scales,
                dec_scales.self_attn_out_scales,
                dec_scales.cross_attn_out_scales,
                dec_scales.ffn_out_scales,
            ):
                layer: T5DecoderLayer
                layer.ln1.eps *= ln1_eps_scale
                layer.ln2.eps *= ln2_eps_scale
                layer.ln3.eps *= ln3_eps_scale
                # make residual smaller at the same time as we make a layer output smaller
                layer.ln1.residual_scale = ln1_residual_scale
                layer.ln2.residual_scale = ln2_residual_scale
                layer.ln3.residual_scale = ln3_residual_scale
            dec.ln.eps *= enc_scales.final_norm_eps_scale

        modules: OrderedDict[str, torch.nn.Module] = OrderedDict()

        if verify_hash is None:
            verify_hash = self._verify_hash

        for name, module in m.named_modules():
            modules[name] = module
        
        keys: tuple[str, ...] = tuple((k for k, *_ in self._metadata.keys()))

        is_ln1 = re.compile(r'layers\.(\d+)\.ln1\.weight$')
        is_ln2 = re.compile(r'layers\.(\d+)\.ln2\.weight$')
        is_ln3 = re.compile(r'layers\.(\d+)\.ln3\.weight$')
        is_o_proj = re.compile(r'layers\.(\d+)\.attn\.o_proj\.weight$')
        is_self_o_proj = re.compile(r'layers\.(\d+)\.self_attn\.o_proj\.weight$')
        is_cross_o_proj = re.compile(r'layers\.(\d+)\.cross_attn\.o_proj\.weight$')
        is_ff_out = re.compile(r'layers\.(\d+)\.ffn\.ff_out\.weight$')
        if fuse_norm_scales:
            enc_keys: tuple[str, ...] = keys if dec is None else tuple((k for k in keys if k.startswith('encoder.')))
            dec_keys: tuple[str, ...] = () if dec is None else tuple((k for k in keys if k.startswith('decoder.')))
            enc_fusions: tuple[FusionSpec, ...] = tuple((FusionSpec(
                norm_weights=norm,
                linear_weights=(lin,),
            ) for norm, lin in (
                *((k, k.replace('ln1', 'attn.qkv_proj')) for k in enc_keys if re.search(is_ln1, k)),
                *((k, k.replace('ln2', 'ffn.ff_in')) for k in enc_keys if re.search(is_ln2, k)),
            )))
            dec_fusions: tuple[FusionSpec, ...] = (
                *(FusionSpec(
                    norm_weights=norm,
                    linear_weights=(lin,),
                ) for norm, lin in (
                    *((k, k.replace('ln1', 'self_attn.qkv_proj')) for k in dec_keys if re.search(is_ln1, k)),
                    *((k, k.replace('ln3', 'ffn.ff_in')) for k in dec_keys if re.search(is_ln3, k)),
                )),
                *(FusionSpec(
                    norm_weights=k,
                    linear_weights=(
                        # fusing into one or the other is sufficient; Qs matmul with Ks anyway,
                        # so the norm scale is shared.
                        k.replace('ln2', 'cross_attn.q_proj'),
                        # k.replace('ln2', 'cross_attn.kv_proj'),
                    ),
                ) for k in dec_keys if re.search(is_ln2, k)),
            )
            fusions: tuple[FusionSpec, ...] = enc_fusions + dec_fusions
            pending_fusions: tuple[FusionTask, ...] = tuple((FusionTask(
                spec=spec,
                awaiting=set((spec.norm_weights, *spec.linear_weights)),
                norm_fusion_via_f32=norm_fusion_via_f32,
            )) for spec in fusions)
            name_to_fusion: dict[str, FusionTask] = {
                name: task for task in pending_fusions for name in task.awaiting
            }
        else:
            name_to_fusion: dict[str, FusionTask] = {}

        tensor_ct = len(keys)

        buffer_type = TensorType.BUFFER
        param_type = TensorType.PARAM
        state_dict_type = TensorType.STATE_DICT

        bulk_loader = self._bulk_load(keys, verify_hash=verify_hash)
        with contextlib.closing(bulk_loader), inference_mode():
            for copied_data in bulk_loader:
                path: _TensorPath = copied_data.header.name
                entry = self._metadata[path]
                if entry.type is state_dict_type:
                    raise NotImplementedError(
                        "This was serialized using"
                        " TensorSerializer.write_state_dict(), so it cannot be"
                        " loaded using TensorDeserializer.load_into_module()."
                        " Use the TensorDeserializer object directly as a"
                        " state_dict mapping instead."
                    )
                elif (
                    entry.type is not buffer_type
                    and entry.type is not param_type
                ):
                    raise RuntimeError(f"Invalid tensor type: {entry.type}")
                elif not path.is_str_:
                    raise NotImplementedError(
                        "Cannot deserialize structured tensor keys as a module;"
                        " try using the TensorDeserializer directly"
                        " as a state_dict mapping instead."
                    )
                tensor = copied_data.parameter
                name: str = path.normalize_()
                obj_path, attr = name.rsplit(".", 1)
                module: torch.nn.Module = modules[obj_path]
                
                # make layer outputs smaller in proportion to how much smaller we made their corresponding residual
                out_scale: Optional[float] = None
                if receives_enc_residual(obj_path):
                    if match := re.search(is_o_proj, name):
                        layer_idx: int = int(match.group(1))
                        out_scale: float = enc_scales.attn_out_scales_cp_hat[layer_idx]
                    elif match := re.search(is_ff_out, name):
                        layer_idx: int = int(match.group(1))
                        out_scale: float = enc_scales.ffn_out_scales_cp_hat[layer_idx]
                if receives_dec_residual(obj_path):
                    if match := re.search(is_self_o_proj, name):
                        layer_idx: int = int(match.group(1))
                        out_scale: float = dec_scales.self_attn_out_scales_cp_hat[layer_idx]
                    elif match := re.search(is_cross_o_proj, name):
                        layer_idx: int = int(match.group(1))
                        out_scale: float = dec_scales.cross_attn_out_scales_cp_hat[layer_idx]
                    elif match := re.search(is_ff_out, name):
                        layer_idx: int = int(match.group(1))
                        out_scale: float = dec_scales.ffn_out_scales_cp_hat[layer_idx]

                if entry.type is param_type:
                    if name in name_to_fusion:
                        task: FusionTask = name_to_fusion[name]
                        completed = task.accept(name, module, attr, tensor)
                        if completed:
                            for name in (task.spec.norm_weights, *task.spec.linear_weights):
                                del name_to_fusion[name]
                    else:
                        if out_scale is not None and out_scale != 1:
                            tensor.mul_(out_scale)
                        module.register_parameter(attr, tensor)
                elif entry.type is buffer_type:
                    module.register_buffer(attr, tensor)

        self._file.close()
        assert not name_to_fusion, f"Unfused: {tuple(name_to_fusion.keys())}"
        return tensor_ct

    
    
