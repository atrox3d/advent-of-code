'''
https://adventofcode.com/2015/day/18
https://adventofcode.com/2015/day/18#part2

--- Day 18: Like a GIF For Your Yard ---
After the million lights incident, the fire code has gotten stricter: now, 
at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal 
lighting configuration. 
With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). 
    
    A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration 
based on the current one. 

  - Each light's next state (either on or off) depends on its current state and the 
    current states of the eight lights adjacent to it (including diagonals). 

  - Lights on the edge of the grid might have fewer than eight neighbors; 
    the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

        1B5...
        234...
        ......
        ..123.
        ..8A4.
        ..765.

The state a light should have next is based on its current state (on or off) plus 
the number of neighbors that are on:

    - A light which is on stays on when 2 or 3 neighbors are on, 
        and turns off otherwise.

    - A light which is off turns on if exactly 3 neighbors are on, 
        and stays off otherwise.

    - All of the lights update simultaneously; 
        they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......
After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, 
how many lights are on after 100 steps?


'''


from pathlib import Path
import logging

logger = logging.getLogger(__name__)

from gridoop import Grid, LineStrategy, CellStrategy

def step(grid:Grid) -> 'Grid':
    '''
The state a light should have next is based on its current state (on or off) plus 
the number of neighbors that are on:

    - A light which is on stays on when 2 or 3 neighbors are on, 
        and turns off otherwise.

    - A light which is off turns on if exactly 3 neighbors are on, 
        and stays off otherwise.

    - All of the lights update simultaneously; 
        they all consider the same current state before moving to the next.

    '''
    grid.print(state=True, end=' ')
    copy = grid.copy()
    for row, col, value in grid.foreach():
        # print(row, col, value)
        state = grid.state(row, col)

        if value == Grid.ON:
            if not 2 <= state <= 3:
                copy.set(row, col, Grid.OFF)

        if value == Grid.OFF:
            if state == 3:
                copy.set(row, col, Grid.ON)
    print()
    copy.print(state=True, end=' ')
    
    return copy

def solution1(quiz_input, test=False):
    grid = Grid(quiz_input, CellStrategy())
    for _ in range(4):
        grid = step(grid)
        print()
    return sum(1 for row, col, light in grid.foreach() if light == Grid.ON )
def solution2(quiz_input, test=False):
    # print(f'{quiz_input = !r}')
    return None

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

class SolutionNotFoundError(Exception): pass
def test(
            path:Path|str,
            part,
            test_file:str=None,
            expected=None
    ):
    logger.info('entering module.test')
    logger.info(f'{locals() = }')
    test_path = path / test_file

    logger.info(f'testing: file {test_path}')
    logger.info(f'testing: {expected = }')
    
    logger.info(f'testing: loading {test_path}')
    test_value = load_input(test_path)
    try:
        logger.info(f'testing: getting solution function')
        solution_name = f'solution{part}'
        solution = globals()[solution_name]
    except KeyError as ke:
        raise SolutionNotFoundError(f'function {solution_name} not found')
    
    logger.info(f'testing: running {solution}')
    result = solution(test_value, test=True)
    result = str(result)
    logger.info(f'testing: evaluating {result=}')
    assert result == expected, f'TEST FAILED: {result=!r} != {expected!r}'
    logger.info('exiting module.test')

if __name__ == '__main__':
    print('please run root main.py')