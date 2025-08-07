#from transformers import GPTNeoForCausalLM, GPT2Tokenizer
#import torch

# Load model and tokenizer
#model_name = "EleutherAI/gpt-neo-125M"  # Can we cache this locally?
#model = GPTNeoForCausalLM.from_pretrained(model_name)
#tokenizer = GPT2Tokenizer.from_pretrained(model_name)

from transformers import pipeline

prompt = \
"""\
Two persons in cloaks traveled a long way to a structure called the Palace. When they got to the front doors, one of the people turned around and lowered her hood, glancing seriously at her partner.

Lumere: Here we are.

Syreal: It’s sublime...

Lumere: I want to show you around inside.

Syreal: Of course!\
"""
chat = prompt
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

while True:
  print(chat)
  print()
  line = input()

  chat += "\n" + line
  resp = generator(chat, max_length=2000, do_sample=True)
  chat = resp[0]['generated_text']
