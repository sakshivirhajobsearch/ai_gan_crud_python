import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from PIL import Image
import os
import random

image_size = 28
latent_dim = 64
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 128),
            nn.ReLU(True),
            nn.Linear(128, image_size*image_size),
            nn.Tanh()
        )

    def forward(self, z):
        img = self.model(z)
        img = img.view(img.size(0), 1, image_size, image_size)
        return img

def generate_image(filename):
    generator = Generator().to(device)
    generator.eval()
    z = torch.randn(1, latent_dim, device=device)
    img = generator(z).detach().cpu()
    img = (img + 1) / 2  # rescale to [0,1]
    img_pil = transforms.ToPILImage()(img.squeeze())
    os.makedirs("static/images", exist_ok=True)
    img_pil.save(f"static/images/{filename}")
    return filename
