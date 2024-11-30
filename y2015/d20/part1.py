from pathlib import Path
import logging

logger = logging.getLogger(__name__)

try:
    import gifts
except:
    from . import gifts

def solve(quiz_input):
    print(f'{quiz_input = !r}')
    max_houses = 1_000_000
    target = int(quiz_input)
    house, presents = gifts.get_house(target, max_houses)
    print(house, presents)
    house, total, houses = gifts.get_house_dict(target)
    return house, total

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
    # with open(filename, 'r') as fp:
        # return fp.read()

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