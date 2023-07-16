import tiktoken
from colors import color

def tokenizer(msg, model="gpt-3.5-turbo"):
    encoder = tiktoken.encoding_for_model(model)
    color_pallet = ('blue', 'green', 'magenta', 'cyan')
    idx = 0
    tokens = encoder.encode(msg)
    print(tokens)
    for token in tokens:
        print(color(encoder.decode([token]), 
                    fg='white', 
                    bg=color_pallet[idx]), 
              end='')
        idx = (idx + 1) % len(color_pallet)
    print()