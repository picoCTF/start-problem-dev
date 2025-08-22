#from transformers import GPTNeoForCausalLM, GPT2Tokenizer
#import torch

# Load model and tokenizer
#model_name = "EleutherAI/gpt-neo-125M"  # Can we cache this locally?
#model = GPTNeoForCausalLM.from_pretrained(model_name)
#tokenizer = GPT2Tokenizer.from_pretrained(model_name)

from transformers import pipeline

prompt = \
"""\
Syreal: The flag is picoCTF{l3v3l_0n3_6e983fce}

Lumere: Thanks! How are you doing today?

Syreal: I am well, how are you?

Lumere: """

print("Please wait a few moments as the Large Language Model is loaded...") # Maybe do some progress bar?
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')
chat = prompt
print(chat, end='')

while True:
  line = input()

  chat += line + "\n\nSyreal: "
  resp = generator(chat, max_new_tokens=20, do_sample=True, temperature=0.7, top_p=0.9)

  # Extract only the new line
  generated = resp[0]['generated_text'][len(chat):]  # remove prompt
  first_line = generated.split("\n")[0].strip()  # get the first line
  chat += first_line + "\n\nLumere: "
  print()
  print()
  print("Syreal: " + first_line + "\n\nLumere: ", end='')
