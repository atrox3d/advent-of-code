from pathlib import Path

with open(Path(__file__).with_suffix('.txt')) as fp:
    input_text = fp.read()

up = input_text.count('(')
down = input_text.count(')')

print(f'{up, down = }')
print(f'{up - down = }')
