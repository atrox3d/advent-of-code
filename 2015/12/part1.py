"""
https://adventofcode.com/2015/day/12
https://adventofcode.com/2015/day/12#part2
"""
import logging
import sys, os
import re, json
from pathlib import Path

# sys.path.append(os.getcwd())
# from aoclib import main

logger = logging.getLogger(__name__)

def solve(data):
    # with open(Path(__file__).parent / 'input.json') as jfp:
    #     data = json.load(jfp)
        # print(json.dumps(data, indent=2))

    def find_numbers(data, skip=None, numbers=None):
        numbers = [] if numbers is None else numbers

        if isinstance(data, int):
            print(f'returning {data}')
            numbers.append(data)
        if isinstance(data, list):
            for element in data:
                find_numbers(element, skip, numbers)
        elif isinstance(data, dict):
            if skip not in data.values():
                for k, v in data.items():
                    find_numbers(v, skip, numbers)
        return numbers
    
    numbers = find_numbers(data)
    # numbersnotred = find_numbers(data, skip='red')
    return sum(numbers)


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
