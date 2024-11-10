"""
https://adventofcode.com/2015/day/8
https://adventofcode.com/2015/day/8#part2
"""
import logging
import sys, os
import re, json
from pathlib import Path
import re

# force import of aoclib
# project_path = Path(__file__).parent.parent.parent
# sys.path.insert(0, str(project_path))
# from aoclib import main

try:
    import compute
except:
    from . import compute


logger = logging.getLogger(__name__)

def solve(quiz_input):
    
    total_chars = compute.get_total_chars(quiz_input)
    print(f'{total_chars = }')

    total_mem = compute.get_total_mem(quiz_input)
    print(f'{total_mem = }')

    total_encoded = compute.get_total_encoded(quiz_input)
    print(f'{total_encoded = }')

    # return total_chars - total_mem, total_encoded - total_chars
    return total_chars - total_mem


def solution(input_path):
    '''called from aoc/main.py'''

    print(f'open {input_path}')
    with open(input_path) as fp:
        input_text = fp.readlines()
    
    print(f'call solve <input_text>')
    result = solve(input_text)
    print(f'{result = }')
    print(f'end solution')

# if __name__ == '__main__':
#     LOGFILE = str(Path(sys.argv[0]).parent / Path(__file__).stem) + '.log'
#     handlers = [
#         logging.FileHandler(LOGFILE, mode='w'),
#         logging.StreamHandler()
#     ]
#     main.main(solution, level='DEBUG', handlers=handlers)
