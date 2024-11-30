'''
https://adventofcode.com/2015/day/15
https://adventofcode.com/2015/day/15#part2
'''

import logging
import sys, os
import re, json
from pathlib import Path

# print(sys.path)
try:
    import ingredient as ing
except:
    from . import ingredient as ing

logger = logging.getLogger(__name__)

def solve(quiz_input, test=False):
    logger.info(f'{quiz_input = !r}')
    # return 222870

    ingredients_properties = ing.parse_ingredients(quiz_input)
    for line in json.dumps(ingredients_properties, indent=2).splitlines():
        logger.info(line)
    
    spoons = 100
    ingredients = 4
    if test:
        # values of the aoc example test
        # testmix = lambda x, y:[(44, 56)]                      
        
        # simulate preceding and subsequent values
        testmix = lambda x, y:[(45, 55), (44, 56), (46, 54)]    
        
        mixes = ing.get_mixes(spoons=spoons, ingredients=ingredients, func=testmix)
    else:
        mixes = ing.get_mixes(spoons=spoons, ingredients=ingredients)
    return ing.get_max_score(mixes, ingredients_properties, 'calories')

def solution(input_path):
    '''called from aoc/main.py'''

    print(f'open {input_path}')
    with open(input_path) as fp:
        input_text = fp.read()
    
    print(f'call solve <input_text>')
    result = solve(input_text)
    print(f'{result = }')
    print(f'end solution')






# def load_input(filename):
#     with open(filename, 'r') as fp:
#         return fp.read()

# def main(
#             path:Path|str,
#             input_file1:str,
#             input_file2:str,
#     ):
#     logger.info('entering module.main')
#     for id, (input_file, solution) in enumerate(zip(
#             (input_file1, input_file2), 
#             (solution1, solution2)
#         ), start=1):
#         input_path = path / input_file
#         logger.info(f'running: file {input_path}')
#         input_value = load_input(input_path)
#         result = solution(input_value)
#         logger.info(f'solution {id}: {result = }')
#     logger.info('exiting module.main')

# class SolutionNotFoundError(Exception): pass
# def test(
#             path:Path|str,
#             part,
#             test_file:str=None,
#             expected=None
#     ):
#     logger.info('entering module.test')
#     test_path = path / test_file

#     logger.info(f'testing: file {test_path}')
#     logger.info(f'testing: {expected = }')
    
#     test_value = load_input(test_path)
#     try:
#         solution_name = f'solution{part}'
#         solution = globals()[solution_name]
#     except KeyError as ke:
#         raise SolutionNotFoundError(f'function {solution_name} not found')
    
#     result = solution(test_value, test=True)
#     result = str(result)
#     assert result == expected, f'TEST FAILED: {result=!r} != {expected!r}'
#     logger.info('exiting module.test')

# if __name__ == '__main__':
#     print('please run root main.py')