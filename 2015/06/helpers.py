from pathlib import Path
import logging

logger = logging.getLogger(__name__)

INPUT_FILE = 'input.txt'
INPUT_PATH = Path(__file__).parent / INPUT_FILE 

def is_multiline(input_path=INPUT_PATH):
    with open(input_path) as fp:
        multiline = '\n' in fp.read()
    logger.debug(f'inputs is {"multiline" if multiline else "just data"}')
    return multiline

def get_input(input_path=INPUT_PATH):
    with open(input_path) as fp:
        data = fp.read()
        if '\n' in data:
            logger.debug(f'parsing input lines')
            data = [line.rstrip() for line in data]
        else:
            logger.debug(f'reading input data')
    return data

def print_input(data=None, input_path=INPUT_PATH):
    logger.debug(f'printing data')
    data = data or get_input(input_path)
    if is_multiline(input_path):
        for line in data:
            print(line)
    else:
        print(data)