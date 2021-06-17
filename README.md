# Wintermute
![image](https://i.imgur.com/hCBb7hX.png)

[![Version](https://img.shields.io/badge/version-1.0-green.svg)](https://huggingface.co/Wintermute/Wintermute)
## What am I?
I am an A.I., created with the OpenAI GPT-2 architecture, and trained with the "Neuromancer" novel by William Gibson.
## What is my purpose ?
To generate text and, with time, improve myself.
## What is this repository?
This repository will contain the source code for the model, as well as the dataset used for training it.

## Using the model
To use Wintermute, do the following:
```python
>>>from transformers import GPT2LMHeadModel, GPT2Tokenizer
>>>tokenizer = GPT2Tokenizer.from_pretrained("Wintermute/Wintermute")
>>>model = GPT2LMHeadModel.from_pretrained("Wintermute/Wintermute")
```
Alternatively, you can run the [wintermute.py](src/wintermute.py) file for an interactive usage of the model:
```python
python wintermute.py
```
## Notes from the author
Currently the model was trained with all books from the Sprawl series.


Due to RAM limitations, I had to train the model with a really small batch-size, so it is still pretty unstable and has a lot of room for improvement. 


If you have any suggestions or ideias, please send them to me at: henriquesoares@dcc.ufmg.br.
