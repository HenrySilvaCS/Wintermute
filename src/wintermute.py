from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch 

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class WINTERMUTE:

    def generate_text(self,text):
        tokenizer = GPT2Tokenizer.from_pretrained("Wintermute/Wintermute")
        model = GPT2LMHeadModel.from_pretrained("Wintermute/Wintermute").to(device)
        input_text = tokenizer(text,return_tensors="pt").to(device) 

        sample_outputs = model.generate(
            input_text.input_ids, #tokenized text input
            do_sample=True, 
            max_length=1000, # max lenght
            min_lenght=30,
            top_k=50, # constant that controls the top-k sampling algorithm
            top_p=0.95, #constant that controls the top-p sampling algorithm
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id
        )
        return tokenizer.decode(sample_outputs[0,:],skip_special_tokens=True)

def main():
    print("This is Wintermute...")
    print("type \"exit()\" to leave...")
    wintermute = WINTERMUTE()
    while True:
        input_text = str(input("Insert text for completion: "))
        if input_text == "exit()":
            print("goodbye...")
            break
        curr_tweet = wintermute.generate_text(input_text)
        while ((len(input_text) + 20) >= (len(curr_tweet))) or (len(curr_tweet) > 280):
            curr_tweet = wintermute.generate_text(input_text)
        print(f"Wintermute: {curr_tweet}")

if __name__ == "__main__":
    main()

