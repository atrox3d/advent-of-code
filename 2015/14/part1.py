"""
https://adventofcode.com/2015/day/14
https://adventofcode.com/2015/day/14#part2
"""
import logging
import sys, os
import re, json
from pathlib import Path

# sys.path.append(os.getcwd())
# from aoclib import main
try:
    import functions
except:
    from . import functions

logger = logging.getLogger(__name__)

def solve(quiz_input):

    reindeers = functions.parse_reindeers(quiz_input)
    # print(reindeers)

    finaltime = 2503
    
    winners = functions.race1(finaltime, reindeers)
    print(winners)
    return winners
    # print(reindeers)
    winner, solution2 = functions.race2(finaltime, reindeers)
    # print(reindeers)
    print(solution2)


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
#     main.main(
#                 solution, 
#                 input_param=None,
#                 test_input=None,
#                 test_expected=None, 
#                 level='INFO', 
#                 handlers=handlers
#             )
