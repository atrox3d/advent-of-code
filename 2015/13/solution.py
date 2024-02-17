"""
https://adventofcode.com/2015/day/13
https://adventofcode.com/2015/day/13#part2
"""
import logging
import sys, os
import re, json
from pathlib import Path

sys.path.append(os.getcwd())
from aoclib import main

logger = logging.getLogger(__name__)

def solution(quiz_input):

    def setup_table(quiz_input: list[str]) -> dict[dict]:
        table = {}
        for line in quiz_input:
            match line.split():
                case name, 'would', op, qty, what, 'units', 'by', 'sitting', 'next', 'to', whom:
                    op = -1 if op == 'lose' else 1
                    qty = int(qty) * op
                    print(f'{name, qty, what, whom = }')
                    table[name] = table.get(name, {})
                    table[name].update({whom:qty})
                case _:
                    raise ValueError()
        return table
    
    table = setup_table(quiz_input)
    print(json.dumps(table, indent=2))


if __name__ == '__main__':
    LOGFILE = str(Path(sys.argv[0]).parent / Path(__file__).stem) + '.log'
    handlers = [
        logging.FileHandler(LOGFILE, mode='w'),
        logging.StreamHandler()
    ]
    main.main(
                solution, 
                input_param=None,
                test_input=None,
                test_expected=None, 
                # level='DEBUG', 
                level='INFO', 
                handlers=handlers
            )
