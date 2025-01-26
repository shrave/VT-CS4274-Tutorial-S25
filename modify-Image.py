import requests
import torch
from PIL import Image
from io import BytesIO
import os

from diffusers import StableDiffusionImg2ImgPipeline

device = "cuda"
model_id_or_path = "OFA-Sys/small-stable-diffusion-v0"
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id_or_path, torch_dtype=torch.float16)
pipe = pipe.to(device)

# Specify the path to the local image in your folder
image_path = "generated_image.png"

# Open the image from the local path
init_image = Image.open(image_path).convert("RGB")
init_image = init_image.resize((768, 512))

# The prompt you want to use for generating a new image
prompt = "A fantasy landscape, trending on artstation"

# Generate the image
images = pipe(prompt=prompt, image=init_image, strength=0.75, guidance_scale=7.5).images

# Save the generated image
images[0].save("fantasy_landscape.png")
