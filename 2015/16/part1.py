from pathlib import Path
import logging
import re

try:
    from auntsue import AuntSue, AuntSue2
    import functions
except: 
    from .auntsue import AuntSue, AuntSue2
    from . import functions

logger = logging.getLogger(__name__)

def solution1(quiz_input):
    aunts = functions.parse_aunts(quiz_input, AuntSue)
    tape = functions.get_tape()

    for auntid, aunt in aunts.items():
        # print(auntid, aunt)
        
        if aunt==tape:
            print(auntid, aunt == tape, '<---------- AUNT SUE!!!!')
            return aunt.id
    

def solution2(quiz_input):
    # return None
    aunts = functions.parse_aunts(quiz_input, AuntSue2)
    tape = functions.get_tape()

    for auntid, aunt in aunts.items():
        # if auntid > 250:
            # break
        # print(auntid, aunt)
        if aunt==tape:
            print(auntid, aunt == tape, '<---------- AUNT SUE!!!!')
            return aunt.id

def solution(input_path):
    '''called from aoc/main.py'''

    print(f'open {input_path}')
    with open(input_path) as fp:
        input_text = fp.read()
    
    print(f'call solve <input_text>')
    result = solution1(input_text)
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
#         print()
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