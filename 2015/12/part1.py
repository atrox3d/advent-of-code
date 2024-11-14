"""
https://adventofcode.com/2015/day/12
https://adventofcode.com/2015/day/12#part2
"""
import logging
import sys, os
import re, json
from pathlib import Path

try:
    from calc import find_numbers
except:
    from .calc import find_numbers

logger = logging.getLogger(__name__)

def solve(data):
    values = find_numbers(data)
    return sum(values)


def solution(input_path):
    '''called from aoc/main.py'''

    print(f'open {input_path}')
    with open(input_path) as fp:
        # input_text = fp.read()
        data = json.load(fp)

    print(f'call solve <input_text>')
    result = solve(data)
    print(f'{result = }')
    print(f'end solution')


# if __name__ == '__main__':
#     LOGFILE = str(Path(sys.argv[0]).parent / Path(__file__).stem) + '.log'
#     handlers = [
#         logging.FileHandler(LOGFILE, mode='w'),
#         logging.StreamHandler()
#     ]
#     main.main(
#                 solution, 
#                 input_param=None,
#                 test_input=None,
#                 test_expected=None, 
#                 level='DEBUG', 
#                 handlers=handlers
#             )
