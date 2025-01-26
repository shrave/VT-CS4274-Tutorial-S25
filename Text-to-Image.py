from diffusers import StableDiffusionPipeline
import torch

# Load pre-trained model
pipe = StableDiffusionPipeline.from_pretrained("OFA-Sys/small-stable-diffusion-v0",
                                         torch_dtype=torch.float16) # You can use different models here
pipe.to("cuda")  # Use GPU if available, otherwise use CPU

# Define your prompt
prompt = "A fantasy landscape with a magical castle, glowing sky, and vibrant colors"

# Generate an image from the prompt
image = pipe(prompt).images[0]

# Save the generated image
image.save("generated_image.png")

# Optionally, display the image
image.show()
