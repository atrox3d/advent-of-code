'''
https://adventofcode.com/2015/day/19
https://adventofcode.com/2015/day/19#part2


--- Day 19: Medicine for Rudolph ---
Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine.

Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need 
custom-made medicine. 
Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, 
capable of constructing any Red-Nosed Reindeer molecule you need. 
It works by starting with some input molecule and then doing a series of replacements, 
one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used.

Calibration involves determining the number of molecules that can be generated 
in one step from a given starting point.

For example, imagine a simpler machine that supports only the following replacements:

H => HO
H => OH
O => HH
Given the replacements above and starting with HOH, the following molecules 
could be generated:

HOOH (via H => HO on the first H).
HOHO (via H => HO on the second H).
OHOH (via H => OH on the first H).
HOOH (via H => OH on the second H).
HHHH (via O => HH).

So, in the example above, there are 4 distinct molecules 
(not five, because HOOH appears twice) after one replacement from HOH. 

Santa's favorite molecule, HOHOHO, can become 7 distinct molecules 
(over nine replacements: six from H, and three from O).

The machine replaces without regard for the surrounding characters. 
For example, given the string H2O, the transition H => OO would result in OO2O.

Your puzzle input describes all of the possible replacements and, at the bottom, 
the medicine molecule for which you need to calibrate the machine. 

How many distinct molecules can be created after all the different ways you can do one 
replacement on the medicine molecule?

'''


from pathlib import Path
import logging

logger = logging.getLogger(__name__)

from calibrator import calibrate
from rules import parse_rules, parse_molecule
def solution1(quiz_input):
    rules = parse_rules(quiz_input)
    start = parse_molecule(quiz_input)
    molecules = calibrate(start, rules)
    return len(molecules)

def solution2(quiz_input):
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
    logger.info(f'SUCCESS')
    logger.info('exiting module.test')

if __name__ == '__main__':
    print('please run root main.py')