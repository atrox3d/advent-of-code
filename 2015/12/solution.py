"""
https://adventofcode.com/2015/day/12
https://adventofcode.com/2015/day/12#part2
"""
import logging
import sys, os
import re, json
from pathlib import Path

sys.path.append(os.getcwd())
from aoclib import main

logger = logging.getLogger(__name__)
def solution(quiz_input):
    with open(Path(__file__).parent / 'input.json') as jfp:
        data = json.load(jfp)
    
    print(json.dumps(data, indent=2))

    # with open(Path(__file__).parent / 'output.json', 'w') as jfp:
        # json.dump(jfp, data, indent=2)



if __name__ == '__main__':
    LOGFILE = str(Path(sys.argv[0]).parent / Path(__file__).stem) + '.log'
    handlers = [
        logging.FileHandler(LOGFILE, mode='w'),
        logging.StreamHandler()
    ]
    main.main(
                solution, 
                input=None,
                test_input=None,
                test_expected=None, 
                level='DEBUG', 
                handlers=handlers
            )
