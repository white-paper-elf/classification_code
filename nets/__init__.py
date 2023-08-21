from .mobilenetv2 import mobilenetv2
from .resnet import resnet18, resnet34, resnet50, resnet101, resnet152
from .vgg import vgg11, vgg13, vgg16, vgg11_bn, vgg13_bn, vgg16_bn
from .vision_transformer import vit_b_16
from .swin_transformer import swin_transformer_base, swin_transformer_small, swin_transformer_tiny
from .mobilenetv3 import mobilenet_v3_large, mobilenet_v3_small
from .models.resnest import resnest50
from .resneXt import resnext50
from .RepVGG import RepVGG_A0, RepVGG_A1, RepVGG_B0, RepVGG_A2, RepVGG_B1g4, RepVGG_B1g2, RepVGG_B1, RepVGG_B2g4, RepVGG_B2, RepVGG_B3g4, RepVGG_B3
get_model_from_name = {
    "mobilenetv2"               : mobilenetv2,
    "resnet18"                  : resnet18,
    "resnet34"                  : resnet34,
    "resnet50"                  : resnet50,
    "resnet101"                 : resnet101,
    "resnet152"                 : resnet152,
    "vgg11"                     : vgg11,
    "vgg13"                     : vgg13,
    "vgg16"                     : vgg16,
    "vgg11_bn"                  : vgg11_bn,
    "vgg13_bn"                  : vgg13_bn,
    "vgg16_bn"                  : vgg16_bn,
    "vit_b_16"                  : vit_b_16,
    "swin_transformer_tiny"     : swin_transformer_tiny,
    "swin_transformer_small"    : swin_transformer_small,
    "swin_transformer_base"     : swin_transformer_base,
    "mobilenetv3_large"         : mobilenet_v3_large,
    "mobilenetv3_small"         : mobilenet_v3_small,
    "RepVGG_B1g2"               : RepVGG_B1g2,
    "resnext50"                 : resnext50,
    "resnest50"                 : resnest50,
}