from pathlib import Path
import logging
import sys

INPUT_FILE = 'input.txt'
INPUT_PATH = Path(sys.argv[0]).parent / INPUT_FILE

logger = logging.getLogger(__name__)

def is_multiline(data=None, input_path=None):
    logger.debug(f'{input_path = }')
    logger.debug(f'{data = }')
    if input_path:
        with open(input_path) as fp:
            data = fp.read()
    if data is not None:
        multiline = '\n' in data
        logger.debug(f'inputs is {"multiline" if multiline else "just data"}')
    else:
        raise ValueError(f'data or input_path needed')
    return multiline

def get_input(input_path):
    logger.debug(f'{input_path = }')
    with open(input_path) as fp:
        data = fp.read()
        logger.debug(f'{data = }')
        if is_multiline(data=data):
            logger.debug(f'parsing input lines')
            data = [line.rstrip() for line in data.split('\n') if line]
        else:
            logger.debug(f'reading input data')
    return data

def print_input(data):
    logger.debug(f'printing {data = }')
    if isinstance(data, list):
        for line in data:
            print(line)
    else:
        print(data)