import logging
import sys
from pathlib import Path

from .loading import get_loader
from ..helpers import datainput

logger = logging.getLogger(__name__)

TESTS_FILE = 'tests.json'
TESTS_PATH = Path(sys.argv[0]).parent / TESTS_FILE

def load_tests(input_path=TESTS_PATH):
    loader = get_loader(input_path)
    return loader(input_path)

def test_param(solution, param: str, input_path: str):
        if not input_path.endswith('.json'):
            if datainput.is_multiline(input_path=input_path):
                logger.debug(f'converting {param} to list')
                param = [param]
        return solution(param)


def test_solution(solution, tests=None, input_path=None):
    tests = load_tests(input_path)

    for test in tests:
        logger.debug(f'{test = }')
        if isinstance(test, tuple|list):
            _input, expected = test
        else:
            raise ValueError(f'test must be a tuple or list {test = }')
        logger.info(f'{_input = }')
        logger.info(f'{expected = }')
        
        # result = test_param(solution, _input)
        result = solution(_input)
        try:
            assert expected == result, f'{expected=} != {result=}'
            logger.info(f'PASS: {expected=} != {result=}')
        except AssertionError as ae:
            logger.error(f'FAIL: {expected=} != {result=}')
        finally:
            print()
