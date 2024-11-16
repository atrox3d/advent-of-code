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

def solution2(quiz_input, test=False):
    '''
    --- Part Two ---
    Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that 
    has exactly 500 calories per cookie (so they can use it as a meal replacement). 
    
    Keep the rest of your award-winning process the same 
            (100 teaspoons, same ingredients, same scoring system).

    For example, given the ingredients above, if you had instead selected 
            40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), 
    the total calorie count would be 
            40*8 + 60*3 = 500. The total score would go down, though: only 57600000, 
    the best you can do in such trying circumstances.

    Given the ingredients in your kitchen and their properties, 
    what is the total score of the highest-scoring cookie you can make with a calorie total of 500?    
    '''
    logger.info(f'{quiz_input = !r}')

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
        testmix = lambda x, y:[(39, 61), (40, 60), (41, 59)]    
        
        mixes = ing.get_mixes(spoons=spoons, ingredients=ingredients, func=testmix)
    else:
        mixes = ing.get_mixes(spoons=spoons, ingredients=ingredients)
    # return ing.get_max_score(mixes, ingredients_properties)
    best_diet_cookies = []
    for total, calories in ing.find_calories(mixes, ingredients_properties, 500):
        print(f'{total=}, {calories=}')
        best_diet_cookies.append({total:calories})
        print(best_diet_cookies)
    print(best_diet_cookies)

    best = max(total for result in best_diet_cookies for total in result)
    print(f'{best=}')




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