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
        return data
    
    def csv_loader(input_path):
        with open(input_path) as fp:
            reader = csv.reader(fp)
            lines = [line for line in reader]
            return lines
        
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

    for _input, expected in tests:
        logger.info(f'testing {_input}: {expected=}')
        result = test_param(solution, _input, multiline)
        try:
            assert expected == result, f'{expected=} != {result=}'
            logger.info(f'PASS: {expected=} != {result=}')
        except AssertionError as ae:
            logger.error(f'FAIL: {expected=} != {result=}')
            # print(repr(ae))
        finally:
            print()
