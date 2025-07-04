import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms, models
from PIL import Image
import matplotlib.pyplot as plt

# Device config
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Image loader
def load_image(img_path, max_size=400):
    image = Image.open(img_path).convert("RGB")

    size = max_size if max(image.size) > max_size else max(image.size)
    transform = transforms.Compose([
        transforms.Resize(size),
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x[:3, :, :]),
        transforms.Normalize((0.485, 0.456, 0.406),
                             (0.229, 0.224, 0.225))  # VGG normalization
    ])

    image = transform(image).unsqueeze(0)
    return image.to(device)

# Image display function
def im_convert(tensor):
    image = tensor.clone().detach().cpu().squeeze(0)
    image = image * torch.tensor([0.229, 0.224, 0.225]).view(3, 1, 1)
    image = image + torch.tensor([0.485, 0.456, 0.406]).view(3, 1, 1)
    image = image.clamp(0, 1)
    return transforms.ToPILImage()(image)

# Load images
content = load_image(r"C:\Users\yashi\Downloads\elite task 3\style_env\content.jpg")

style = load_image(r"C:\Users\yashi\Downloads\elite task 3\style_env\style.jpg")


from torchvision.models import vgg19, VGG19_Weights
vgg = vgg19(weights=VGG19_Weights.DEFAULT).features.to(device).eval()


# Freeze all VGG params
for param in vgg.parameters():
    param.requires_grad_(False)

# Content and Style layers
content_layers = ['conv4_2']
style_layers = ['conv1_1', 'conv2_1', 'conv3_1', 'conv4_1', 'conv5_1']

# Get layers from VGG
def get_features(image, model, layers=None):
    features = {}
    x = image
    for name, layer in model._modules.items():
        x = layer(x)
        if layers and name in layers:
            features[layers[name]] = x
    return features

# Layer mapping
layer_mapping = {
    '0': 'conv1_1',
    '5': 'conv2_1',
    '10': 'conv3_1',
    '19': 'conv4_1',
    '21': 'conv4_2',
    '28': 'conv5_1'
}

# Extract features
content_features = get_features(content, vgg, {k: v for k, v in layer_mapping.items() if v in content_layers})
style_features = get_features(style, vgg, {k: v for k, v in layer_mapping.items() if v in style_layers})

# Gram matrix for style
def gram_matrix(tensor):
    _, d, h, w = tensor.size()
    tensor = tensor.view(d, h * w)
    return torch.mm(tensor, tensor.t())

# Style Gram matrices
style_grams = {layer: gram_matrix(style_features[layer]) for layer in style_features}

# Input image (start with content)
target = content.clone().requires_grad_(True).to(device)

# Optimizer
optimizer = optim.Adam([target], lr=0.003)

# Weights
style_weights = {
    'conv1_1': 1.0,
    'conv2_1': 0.75,
    'conv3_1': 0.2,
    'conv4_1': 0.2,
    'conv5_1': 0.2
}
content_weight = 1  # alpha
style_weight = 1e6  # beta

# Training loop
epochs = 500
for i in range(epochs):
    target_features = get_features(target, vgg, {k: v for k, v in layer_mapping.items()})
    
    content_loss = torch.mean((target_features['conv4_2'] - content_features['conv4_2']) ** 2)
    
    style_loss = 0
    for layer in style_weights:
        target_feature = target_features[layer]
        target_gram = gram_matrix(target_feature)
        style_gram = style_grams[layer]
        layer_loss = style_weights[layer] * torch.mean((target_gram - style_gram) ** 2)
        style_loss += layer_loss
    
    total_loss = content_weight * content_loss + style_weight * style_loss
    
    optimizer.zero_grad()
    total_loss.backward()
    optimizer.step()
    
    if i % 50 == 0:
        print(f"Iteration {i}, Total loss: {total_loss.item()}")

# Show final result
plt.imshow(im_convert(target))
plt.title("Stylized Image")
plt.axis("off")
plt.show()
