from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def solution1(quiz_input):
    print(f'{quiz_input = !r}')
    return None

def solution2(quiz_input):
    print(f'{quiz_input = !r}')
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
    if expected is not None:
        test_path = path / test_file
        logger.info(f'testing: file {test_path}')
        logger.info(f'testing: {expected = }')
        test_value = load_input(test_path)
        result = solution(test_value)
        assert result == expected, f'TEST FAILED: {result=} != {expected}'
    else:
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
