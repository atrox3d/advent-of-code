"""
https://adventofcode.com/2015/day/8
https://adventofcode.com/2015/day/8#part2
"""
import logging
import sys, os
import re, json
from pathlib import Path
import re

sys.path.insert(0, os.getcwd())
from aoclib import main

logger = logging.getLogger(__name__)

def solution(quiz_input):
    
    total_chars = sum(len(s) for s in quiz_input)
    print(total_chars)

    total_mem = sum(len(eval(s)) for s in quiz_input)
    print(total_mem)

    total_encoded = sum(len(json.dumps(line)) for line in quiz_input)
    print(total_encoded)

    return total_chars - total_mem, total_encoded - total_chars

if __name__ == '__main__':
    LOGFILE = str(Path(sys.argv[0]).parent / Path(__file__).stem) + '.log'
    handlers = [
        logging.FileHandler(LOGFILE, mode='w'),
        logging.StreamHandler()
    ]
    main.main(solution, level='DEBUG', handlers=handlers)
