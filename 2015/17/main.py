'''
https://adventofcode.com/2015/day/17
https://adventofcode.com/2015/day/17#part2

--- Day 17: No Such Thing as Too Much ---
The elves bought too much eggnog again - 150 liters this time. To fit it all into 
your refrigerator, you'll need to move it into smaller containers. 
You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. 
If you need to store 25 liters, there are four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5

Filling all containers entirely, how many different combinations of containers 
can exactly fit all 150 liters of eggnog?

--- Part Two ---
While playing with all the containers in the kitchen, another load of eggnog arrives! 
The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog. 
How many different ways can you fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. 
There were three ways to use that many containers, 
and so the answer there would be 3.
'''


from pathlib import Path
import logging

import eggnog

logger = logging.getLogger(__name__)

example = 25, [20, 15, 10, 5, 5]
    
    
def solution1(quiz_input):
    print(f'{quiz_input = !r}')

    values = load_array(quiz_input)
    result = eggnog.subset_sum(150, values)
    print(len(result))
    return len(result)


def solution2(quiz_input):
    print(f'{quiz_input = !r}')

    values = load_array(quiz_input)
    print(values)
    result = eggnog.subset_sum(150, values)
    # print(result)
    minimum = min(map(len, result))
    count = len([x for x in map(len, result) if x == minimum])
    print(count)
    return count

def load_input(filename):
    with open(filename, 'r') as fp:
        return fp.read()

def load_array(quiz_input:str) ->list[int]:
    return [int(line) for line in quiz_input.splitlines()]

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
        print()
        print()
    logger.info('exiting module.main')

class SolutionNotFoundError(Exception): pass
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
    try:
        solution_name = f'solution{part}'
        solution = globals()[solution_name]
    except KeyError as ke:
        raise SolutionNotFoundError(f'function {solution_name} not found')
    
    result = solution(test_value, test=True)
    result = str(result)
    assert result == expected, f'TEST FAILED: {result=!r} != {expected!r}'
    logger.info('exiting module.test')

if __name__ == '__main__':
    print('please run root main.py')