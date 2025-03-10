import os

import torch
import torchvision.transforms as transforms
from torchinfo import summary

import PIL.Image as Image
import matplotlib.pyplot as plt


def viz(layer_num, img_path, model, device):
    """Display a visualization of CNN feature map

    Display convolutional neural network CNN feature maps of specified ``layer`` given ``image path`` and ``model``.

    Parameters
    ----------
    layer_num : int
        Layer number of CNN to visualize.
    img_path : str
        Path to input image.
    model
        PyTorch CNN model
    device : str
        Device to run inference on exp. ``cuda:0`` or ``cpu``

    Examples
    --------
    >>> from opengenome.outputs.cnn import viz
    >>> import torch
    >>> from torchvision.models import vgg16, VGG16_Weights
    >>> DEVICE = 'cuda:0' if torch.cuda.is_available() else 'cpu'
    >>> model = vgg16(weights=VGG16_Weights.DEFAULT)
    >>> model = model.to(DEVICE)
    >>> img_car = r"PATH_TO_IMAGE"
    >>> viz(10, img_car, model, DEVICE) 
    """
    # transforms_vgg16 = VGG16_Weights.IMAGENET1K_V1.transforms
    transforms_vgg16 = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.485, 0.456, 0.406),
                             std=(0.229, 0.224, 0.225))
    ])

    summary(model=model, input_size=(1, 3, 224, 224))

    img_path = Image.open(img_path).convert('RGB')
    img_path = transforms_vgg16(img_path).unsqueeze(dim=0)
    img_path = img_path.to(device)

    layer = model.features[layer_num]
    print(layer)

    # define hook to return output feature map at layer n
    feature_maps = []

    def hook_fn(module, input, output):
        feature_maps.append(output)

    # register the hook
    handle = layer.register_forward_hook(hook_fn)

    model.eval()
    with torch.inference_mode():
        preds = model(img_path)

    pred_cls = preds.argmax(dim=1)
    classes_imgnet_txt = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data",
                     "VGG16_CLASSES.txt"))
    with open(classes_imgnet_txt, 'r') as f:
        classes_imgnet = f.readlines()
    pred_cls = classes_imgnet[pred_cls]
    print(pred_cls)

    layer_output = feature_maps[0].squeeze()
    rows, cols = 4, 6
    fig = plt.figure(figsize=(10, 6))
    for i in range(1, (rows * cols) + 1):
        feature_map = layer_output[i - 1, :, :].cpu().numpy()
        fig.add_subplot(rows, cols, i)
        plt.imshow(feature_map, cmap='viridis')
        plt.tight_layout()
        plt.axis(False)

    plt.show()
