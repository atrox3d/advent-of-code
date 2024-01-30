from pathlib import Path

with open(Path(__file__).parent / 'input.txt') as fp:
    print(fp.read())