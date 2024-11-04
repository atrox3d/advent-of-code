from pathlib import Path

def solution(input_path):
    with open(input_path) as fp:
        input_text = fp.read()
    
    up = input_text.count('(')
    down = input_text.count(')')

    print(f'{up, down = }')
    print(f'{up - down = }')
