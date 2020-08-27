# Wintermute
![image](https://i.imgur.com/hCBb7hX.png)
## What am I?
I am an A.I., created with the OpenAI GPT-2 architecture, and trained with the "Neuromancer" novel by William Gibson.
## What is my purpose ?
To generate text and, with time, improve myself to produce a coherent chapter based on Neuromancer.
## What is this repository?
This repository will contain the source code for the model, as well as the dataset used for training it.

## Using the model
To use Wintermute, do the following:
```python
>>>pip install transformers
>>>from transformers import GPT2LMHeadModel, GPT2Tokenizer
>>>tokenizer = GPT2Tokenizer.from_pretrained("Wintermute/Wintermute")
>>>model = GPT2LMHeadModel.from_pretrained("Wintermute/Wintermute")
```
## On Hugging Face
[Link to the hugging face page](https://huggingface.co/Wintermute/Wintermute)
## Notes from the author
Currently the model was trained with only the first book of the Sprawl Series, but I intend to train it with more data in the future. 


Due to RAM limitations, I had to train the model with a really small batch-size, so it is still pretty unstable and has a lot of room for improvement. 


If you have any suggestions or ideias, please send them to me at: henriquesoares@dcc.ufmg.br or at my twitter: @vaitomarnomidia.
