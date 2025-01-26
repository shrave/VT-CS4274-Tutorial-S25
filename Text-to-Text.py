from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the GPT-2 model and tokenizer
model_name = "gpt2"  # Can be "distilgpt2" for the smaller version or "gpt2-medium" for a larger one
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Define the prompt
prompt = "The future of artificial intelligence is"

# Tokenize the prompt
inputs = tokenizer(prompt, return_tensors="pt")

# Generate text from the model
output = model.generate(inputs["input_ids"], max_length=100, num_return_sequences=1)

# Decode the output
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

# Print the generated text
print(generated_text)
