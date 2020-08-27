import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, PretrainedConfig

###
config = PretrainedConfig.from_pretrained('model/config.json')
model = GPT2LMHeadModel(config).from_pretrained('gpt2').from_pretrained('model/gpt2_neuromancer_parameters')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')



text = input("Input text for batch inference: ")

inputs = tokenizer(text, return_tensors="pt")

sample_outputs = model.generate(
    inputs.input_ids,
    do_sample=True, 
    max_length=120, 
    top_k=50, 
    top_p=0.95, 
    num_return_sequences=10
)

for i, sample_output in enumerate(sample_outputs):
    print(">> Generated text {}\n\n{}".format(i+1, tokenizer.decode(sample_output.tolist(),skip_special_tokens=True)))
    print("\n")



####

