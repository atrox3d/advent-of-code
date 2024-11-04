from pathlib import Path
import os
import time

def solution(input_path:str):
    with open(input_path) as fp:
        input_text = fp.read()

    floor = 0
    for pos, char in enumerate(input_text):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            print(pos + 1)
            break