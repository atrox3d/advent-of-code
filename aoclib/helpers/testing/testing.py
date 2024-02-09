import logging
import json
import csv
import sys
from pathlib import Path

from .. import datainput

logger = logging.getLogger(__name__)

TESTS_FILE = 'tests.json'
TESTS_PATH = Path(sys.argv[0]).parent / TESTS_FILE

def get_loader(input_path):
    def json_loader(input_path):
        with open(input_path) as fp:
            data = json.load(fp)
            logger.debug(f'{data = }')
            for d in data:
                for k, v in d.items():
                    if '\n' in v:
                        d[k] = [line for line in v.split('\n') if line]
            logger.debug(f'{data = }')
            data = [tuple(item.values()) for item in data]
            logger.debug(f'{data = }')
        return data
    
    def str_to_val(value):
        if value.isnumeric():
            value = int(value)
        elif value.lower() in ('true', 'false'):
            value = bool(value)
        elif value.lower() == 'none':
            value = None
        return value
    
    def csv_loader(input_path):
        with open(input_path) as fp:
            reader = csv.reader(fp,)
            lines = [list(map(str.strip, line)) for line in reader]
            logger.debug(f'{lines = }')
            convert = [[str_to_val(value) for value in values] for values in lines]
            return convert
            
    suffix = Path(input_path).suffix
    if suffix == '.json':
        logger.info(f'json loader')
        return json_loader
    elif suffix == '.csv':
        logger.info(f'csv loader')
        return csv_loader
    else:
        raise NotImplementedError(f'file type {suffix} not implemented')


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
            raise ValueError(f'tes must be a tuple or list {test = }')
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
