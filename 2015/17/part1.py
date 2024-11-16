from pathlib import Path
import logging

try:
    import eggnog
except:
    from . import eggnog

logger = logging.getLogger(__name__)

example = 25, [20, 15, 10, 5, 5]
    
    
def solve(quiz_input):
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
#         print()
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