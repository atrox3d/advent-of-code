import logging
import json
import csv
from pathlib import Path

import helpers

logger = logging.getLogger(__name__)

TESTS_FILE = 'tests.json'
TESTS_PATH = Path(__file__).parent / TESTS_FILE

def test_param(solution, param, multiline):
        if multiline:
            logger.debug(f'converting {param} to list')
            param = [param]
        return solution(param)

def get_loader(input_path):
    def json_loader(input_path):
        with open(input_path) as fp:
            data = json.load(fp)
            data = [tuple(data.values()) for data in data]
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
            convert = []
            for values in lines:
                cvalues = []
                for value in values:
                    cvalues.append(str_to_val(value))
                convert.append(cvalues)
            return convert
        
    def txt_loader(input_path):
        with open(input_path) as fp:
            lines = [line.strip() for line in fp.readlines()]
            return lines
            
    suffix = Path(input_path).suffix
    if suffix == '.json':
        logger.info(f'json loader')
        return json_loader
    elif suffix == '.csv':
        logger.info(f'csv loader')
        return csv_loader
    elif suffix == '.txt':
        logger.info(f'txt loader')
        return txt_loader
    else:
        raise NotImplementedError(f'file type {suffix} not implemented')


def load_tests(input_path=TESTS_PATH):
    loader = get_loader(input_path)
    return loader(input_path)


def test(solution, tests=None, input_path=None, multiline=None):
    tests = load_tests(input_path)

    for test in tests:
        logger.debug(f'{test = }')
        if isinstance(test, tuple|list):
            _input, expected = test
        else:
            raise ValueError(f'tes must be a tuple or list {test = }')
        logger.info(f'testing {_input=}: {expected=}')
        
        result = test_param(solution, _input, multiline)
        try:
            assert expected == result, f'{expected=} != {result=}'
            logger.info(f'PASS: {expected=} != {result=}')
        except AssertionError as ae:
            logger.error(f'FAIL: {expected=} != {result=}')
            # print(repr(ae))
        finally:
            print()
