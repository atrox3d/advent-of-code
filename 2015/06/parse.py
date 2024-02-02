import argparse

import helpers

def get_parser() -> argparse.ArgumentParser:
    # create parser
    parser = argparse.ArgumentParser(
        description="aoc parser"
    )
    parser.add_argument('test_val', nargs='?')
    
    mutex = parser.add_mutually_exclusive_group()
    mutex.add_argument('-p', '--print', action='store_true')
    mutex.add_argument('-t', '--test',  action='store_true')
    
    parser.add_argument('-i', '--input_path', default=helpers.INPUT_PATH)
    return parser
