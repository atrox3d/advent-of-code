from pathlib import Path

def solution(input_path:str=None):
    if input_path is None:
        input_path = Path(__file__).with_suffix('.txt')
    
    with open(input_path) as fp:
        input_text = fp.read()
    
    up = input_text.count('(')
    down = input_text.count(')')

    print(f'{up, down = }')
    print(f'{up - down = }')
