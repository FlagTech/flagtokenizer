import tiktoken
from colors import color

def tokenizer(msg, model="gpt-3.5-turbo", show=True):
    encoder = tiktoken.encoding_for_model(model)
    color_pallet = (                
        '#FFB347', # Pastel orange (淡橙色)
        '#FFCC99', # Peach (桃色)
        '#FFFF66', # Pastel yellow (淡黃色)
        '#64fa64', # Tea green (茶綠色)
        '#CCFFCC', # Aero blue (天青色)
        '#CB99C9', # Thistle (薊色)
        '#FFB6C1', # Light pink (淺粉紅色)
        '#FFCCDD', # Pink lace (粉翠珠色)
        '#CCCCFF'  # Lavender blue (薰衣草藍)
    )
    idx = 0
    tokens = encoder.encode(msg)
    if show:
        for token in tokens:
            print(color(encoder.decode([token]), 
                        fg='black',
                        bg=color_pallet[idx]), 
                end='')
            idx = (idx + 1) % len(color_pallet)
        print()
    return tokens