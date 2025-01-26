from diffusers import StableDiffusionPipeline, DiffusionPipeline
import torch

# Load pre-trained model
# model_id = "CompVis/stable-diffusion-v1-4-original"  # You can use different models here
# pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = StableDiffusionPipeline.from_pretrained("OFA-Sys/small-stable-diffusion-v0",
                                         torch_dtype=torch.float16)
pipe.to("cuda")  # Use GPU if available, otherwise use CPU

# Define your prompt
prompt = "A fantasy landscape with a magical castle, glowing sky, and vibrant colors"

# Generate an image from the prompt
image = pipe(prompt).images[0]

# Save the generated image
image.save("generated_image.png")

# Optionally, display the image
image.show()
