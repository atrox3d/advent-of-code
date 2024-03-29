import argparse
import logging

from . import datainput
from ..testing import testing

logger = logging.getLogger(__name__)

def get_parser() -> argparse.ArgumentParser:
    # create parser
    parser = argparse.ArgumentParser(description="aoc parser")
    parser.add_argument('test_param', nargs='?')
    
    # mutex = parser.add_mutually_exclusive_group()
    parser.add_argument('-p', '--print', action='store_true', help='print input')
    parser.add_argument('-t', '--test_path', help='test against file')
    parser.add_argument('-e', '--expected', help='expected result fot -t')
    
    # default with no args
    parser.add_argument('-i', '--input_path', help='run against file (DEFAULT)',
                        default=datainput.INPUT_PATH)
    return parser

def log_cmdline_options(options: argparse.Namespace, log=logger.info):
    for k, v in vars(options).items():
        log(f'{k} = {v}')
    
if __name__ == '__main__':
    print(get_parser().parse_args())
