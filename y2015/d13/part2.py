"""
https://adventofcode.com/2015/day/13
https://adventofcode.com/2015/day/13#part2
"""
import logging
import sys, os
import re, json
from pathlib import Path

logger = logging.getLogger(__name__)

try:
    from happiness import get_happiness, totals, rpermute
except:
    from .happiness import get_happiness, totals, rpermute

def solve(quiz_input):

    happiness = get_happiness(quiz_input)
    print('happiness=', json.dumps(happiness, indent=2))

    names = [name for name in happiness]
    permutations = rpermute(names)
    combos = [item for item in permutations if item[0]==names[0]]

    # best = (max(totals(happiness, combos)))
    # print(best)
    # return best

    me = {}
    for name in happiness:
        me.update({name:0})
    happiness['me'] = me
    for name in happiness:
        happiness[name].update({'me':0})
    print('happiness=', json.dumps(happiness, indent=2))

    names = [name for name in happiness]
    permutations = rpermute(names)
    combos = [item for item in permutations if item[0]==names[0]]

    bestme = (max(totals(happiness, combos)))
    print(bestme)

    return bestme

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
#                 # level='DEBUG', 
#                 level='INFO', 
#                 handlers=handlers
#             )
