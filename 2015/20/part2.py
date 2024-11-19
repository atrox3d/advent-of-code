'''
https://adventofcode.com/2015/day/20
https://adventofcode.com/2015/day/20#part2

--- Day 20: Infinite Elves and Infinite Houses ---
To keep the Elves busy, Santa has them deliver some presents 
by hand, door-to-door. 
He sends them down a street with infinite houses numbered 
sequentially: 1, 2, 3, 4, 5, and so on.

Each Elf is assigned a number, too, 
and delivers presents to houses based on that number:

The first Elf (number 1) delivers presents to every house:
 1, 2, 3, 4, 5, ....

The second Elf (number 2) delivers presents to every second house:
 2, 4, 6, 8, 10, ....

Elf number 3 delivers presents to every third house:
 3, 6, 9, 12, 15, ....

There are infinitely many Elves, numbered starting with 1. 
Each Elf delivers presents equal to ten times his or her number 
at each house.

So, the first nine houses on the street end up like this:

House 1 got 10 presents.
House 2 got 30 presents.
House 3 got 40 presents.
House 4 got 70 presents.
House 5 got 60 presents.
House 6 got 120 presents.
House 7 got 80 presents.
House 8 got 150 presents.
House 9 got 130 presents.

The first house gets 10 presents: it is visited only by Elf 1, 
which delivers 1 * 10 = 10 presents. 
The fourth house gets 70 presents, because it is visited by Elves 
1, 2, and 4, for a total of 10 + 20 + 40 = 70 presents.

What is the lowest house number of the house to get at least as
many presents as the number in your puzzle input?

Your puzzle input is 33100000.

'''
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

import gifts


# def load_input(filename):
    # with open(filename, 'r') as fp:
        # return fp.read()

def solve(quiz_input):
    print(f'{quiz_input = !r}')
    max_houses = 1_000_000
    target = int(quiz_input)
    house, presents = gifts.get_house(target, max_houses, 11, 50)
    print(house, presents)
    return house

def solution(input_path):
    '''called from aoc/main.py'''

    print(f'open {input_path}')
    with open(input_path) as fp:
        input_text = fp.read()
    
    print(f'call solve <input_text>')
    result = solve(input_text)
    print(f'{result = }')
    print(f'end solution')

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
#         print('\n')

#     logger.info('exiting module.main')

# class SolutionNotFoundError(Exception): pass
# def test(
#             path:Path|str,
#             part,
#             test_file:str=None,
#             expected=None
#     ):
#     logger.info('entering module.test')
#     logger.info(f'{locals() = }')
#     test_path = path / test_file

#     logger.info(f'testing: file {test_path}')
#     logger.info(f'testing: {expected = }')
    
#     logger.info(f'testing: loading {test_path}')
#     test_value = load_input(test_path)
#     try:
#         logger.info(f'testing: getting solution function')
#         solution_name = f'solution{part}'
#         solution = globals()[solution_name]
#     except KeyError as ke:
#         raise SolutionNotFoundError(f'function {solution_name} not found')
    
#     logger.info(f'testing: running {solution}')
#     result = solution(test_value, test=True)
#     result = str(result)
#     logger.info(f'testing: evaluating {result=}')
#     assert result == expected, f'TEST FAILED: {result=!r} != {expected!r}'
#     logger.info(f'SUCCESS')
#     logger.info('exiting module.test')

# if __name__ == '__main__':
#     print('please run root main.py')