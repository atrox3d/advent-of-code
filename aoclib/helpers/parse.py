import argparse
import logging

from . import datainput
from ..testing import testing

logger = logging.getLogger(__name__)

def get_parser() -> argparse.ArgumentParser:
    # create parser
    parser = argparse.ArgumentParser(description="aoc parser")
    parser.add_argument('test_param', nargs='?')
    
    mutex = parser.add_mutually_exclusive_group()
    mutex.add_argument('-p', '--print', action='store_true')
    mutex.add_argument('-t', '--test', nargs='?', default=None, 
                       const=testing.TESTS_PATH)
    
    parser.add_argument('-i', '--input_path', 
                        default=datainput.INPUT_PATH)
    return parser

def log_options(options: argparse.Namespace):
    for k, v in vars(options).items():
        logger.debug(f'{k} = {v}')
    
if __name__ == '__main__':
    print(get_parser().parse_args())