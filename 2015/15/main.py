'''
https://adventofcode.com/2015/day/15
https://adventofcode.com/2015/day/15#part2
'''

import logging
import sys, os
import re, json
from pathlib import Path

print(sys.path)
import ingredient as ing

logger = logging.getLogger(__name__)

def solution1(quiz_input, test=False):
    '''
    --- Day 15: Science for Hungry People ---
    Today, you set out on the task of perfecting your milk-dunking cookie recipe. 
    All you have to do is find the right balance of ingredients.

    Your recipe leaves room for exactly 100 teaspoons of ingredients. 
    You make a list of the remaining ingredients you could use to finish the recipe 
    (your puzzle input) and their properties per teaspoon:

    capacity (how well it helps the cookie absorb milk)
    durability (how well it keeps the cookie intact when full of milk)
    flavor (how tasty it makes the cookie)
    texture (how it improves the feel of the cookie)
    calories (how many calories it adds to the cookie)
    You can only measure ingredients in whole-teaspoon amounts accurately, 
    and you have to be accurate so you can reproduce your results in the future. 
    The total score of a cookie can be found by adding up each of the properties 
    (negative totals become 0) and then multiplying together everything except calories.

    For instance, suppose you have these two ingredients:

    - Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
    - Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

    - Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon 
    (because the amounts of each ingredient must add up to 100) 
    would result in a cookie with the following properties:

    A capacity of 44*-1 + 56*2 = 68
    A durability of 44*-2 + 56*3 = 80
    A flavor of 44*6 + 56*-2 = 152
    A texture of 44*3 + 56*-1 = 76

    Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) 
    results in a total score of 62842880, 
    which happens to be the best score possible given these ingredients. 
    If any properties had produced a negative total, 
    it would have instead become zero, causing the whole score to multiply to zero.

    Given the ingredients in your kitchen and their properties, 
    what is the total score of the highest-scoring cookie you can make?    
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
        
        mixes = ing.get_mixes(spoons=spoons, ingredients=ingredients, func=testmix)
    else:
        mixes = ing.get_mixes(spoons=spoons, ingredients=ingredients)

    return ing.get_max_score(mixes, ingredients_properties)


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
        
        mixes = ing.get_mixes(spoons=spoons, ingredients=ingredients, func=testmix)
    else:
        mixes = ing.get_mixes(spoons=spoons, ingredients=ingredients)
    return ing.get_max_score(mixes, ingredients_properties)

def load_input(filename):
    with open(filename, 'r') as fp:
        return fp.read()

def main(
            path:Path|str,
            input_file1:str,
            input_file2:str,
    ):
    logger.info('entering module.main')
    for id, (input_file, solution) in enumerate(zip(
            (input_file1, input_file2), 
            (solution1, solution2)
        ), start=1):
        input_path = path / input_file
        logger.info(f'running: file {input_path}')
        input_value = load_input(input_path)
        result = solution(input_value)
        logger.info(f'solution {id}: {result = }')
    logger.info('exiting module.main')

def test(
            path:Path|str,
            part,
            test_file:str=None,
            expected=None
    ):
    logger.info('entering module.test')
    test_path = path / test_file
    logger.info(f'testing: file {test_path}')
    logger.info(f'testing: {expected = }')
    test_value = load_input(test_path)
    solution = globals()[f'solution{part}']
    result = solution(test_value, test=True)
    result = str(result)
    assert result == expected, f'TEST FAILED: {result=!r} != {expected!r}'
    logger.info('exiting module.test')
