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
            expected1,
            input_file2:str,
            expected2,
    ):
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
