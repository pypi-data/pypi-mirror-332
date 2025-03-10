import torch
import torch.nn as nn
from torchvision import models


def get_model(name: str='fcn_resnet50', num_classes: int=3, pretrained: bool=True, weights: str=None) -> torch.nn.Module:
	""" Load a segmentation model from torchvision.models.segmentation.

	Args:
		name (str): Model name. Default is 'fcn_resnet50'.
		num_classes (int): Number of classes. Default is 3.
		pretrained (bool): Use a pretrained model. Default is True.
		weights (str): Path to model weights. Default is None.

	Returns:
		torch.nn.Module: Segmentation model.

	Raises:
		ValueError: If the model name is not supported.
	"""
	match name:
		case 'fcn_resnet50':
			model = models.segmentation.fcn_resnet50(pretrained=pretrained, weights='DEFAULT')
		case 'fcn_resnet101':
			model = models.segmentation.fcn_resnet101(pretrained=pretrained, weights='DEFAULT')
		case 'deeplabv3_resnet101':
			model = models.segmentation.deeplabv3_resnet101(pretrained=pretrained, weights='DEFAULT')
		case 'deeplabv3_resnet50':
			model = models.segmentation.deeplabv3_resnet50(pretrained=pretrained, weights='DEFAULT')
		case 'deeplabv3_mobilenet_v3_large':
			model = models.segmentation.deeplabv3_mobilenet_v3_large(pretrained=pretrained, weights='DEFAULT')
		case _:
			raise ValueError(f"Model {name} not supported")

	model.classifier[4] = nn.LazyConv2d(num_classes, 1)
	model.aux_classifier[4] = nn.LazyConv2d(num_classes, 1)

	if weights is not None:
		model.load_state_dict(torch.load(weights))

	model = model.half()
	return model
