from pathlib import Path
import logging

INPUT_FILE = 'input.txt'
INPUT_PATH = Path(__file__).parent / INPUT_FILE 

logger = logging.getLogger(__name__)

def is_multiline(data=None, input_path=None):
    if input_path:
        with open(input_path) as fp:
            data = fp.read()
    if data:
        multiline = '\n' in data
        logger.debug(f'inputs is {"multiline" if multiline else "just data"}')
    else:
        raise ValueError(f'data or input_path needed')
    return multiline

def get_input(input_path):
    with open(input_path) as fp:
        data = fp.read()
        if is_multiline(data=data):
            logger.debug(f'parsing input lines')
            data = [line.rstrip() for line in data.split('\n')]
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