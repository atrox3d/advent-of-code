'''
https://adventofcode.com/2015/day/15
https://adventofcode.com/2015/day/15#part2
'''

import logging
import sys, os
import re, json
from pathlib import Path

logger = logging.getLogger(__name__)

def load_ingredients(quiz_input:str) -> dict:
    import re
    pattern = r'(?P<name>\w+): capacity (?P<capacity>-?\d+), '\
            r'durability (?P<durability>-?\d+), flavor (?P<flavor>-?\d+), '\
            r'texture (?P<texture>-?\d+), calories (?P<calories>-?\d+)'
    ingredients = {}
    for line in quiz_input.splitlines():
        match = re.match(pattern, line)
        temp = match.groupdict()
        ingredients[temp['name']] = {k:v for k, v in temp.items() if k != 'name'}
    return ingredients

def solution1(quiz_input):
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

    ingredients = load_ingredients(quiz_input)
    for line in json.dumps(ingredients, indent=2).splitlines():
        logger.info(line)
    
    return None

def solution2(quiz_input):
    logger.info(f'{quiz_input = !r}')
    return None

def load_input(filename):
    with open(filename, 'r') as fp:
        return fp.read()

def main(
            path:Path|str,
            input_file1:str,
            # expected1,
            input_file2:str,
            # expected2,
            # solve_first:bool=False, 
            # solve_second:bool=False, 
            test_file:str=None,
            expected=None
    ):
    logger.info('entering module.main')
    for id, (input_file, solution) in enumerate(zip(
            (input_file1, input_file2), 
            (solution1, solution2)
        ), start=1):
        input_path = path / input_file
        input_value = load_input(input_path)
        result = solution(input_value)
        logger.info(f'solution {id}: {result = }')
    logger.info('exiting module.main')
    
    return
    # this is testing, not solving
    # TODO: implement testing
    for input_file, expected, solution in zip(
            (input_file1, input_file2), 
            (expected1, expected2),
            (solution1, solution2)
        ):
        input_path = path / input_file
        input_value = load_input(input_path)
        result = solution(input_value)
        if expected is not None:
            assert result == expected, f'{result=} != {expected}'
        else:
            logger.info(f'{result = }')
