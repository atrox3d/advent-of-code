"""
https://adventofcode.com/2015/day/10
https://adventofcode.com/2015/day/10#part2
"""
import logging
import sys, os
import re, json
from pathlib import Path

sys.path.append(os.getcwd())
from aoclib import main

logger = logging.getLogger(__name__)

def solution(quiz_input):
    '''
    --- Day 10: Elves Look, Elves Say ---
    Today, the Elves are playing a game called look-and-say. 
    They take turns making sequences by reading aloud the previous 
    sequence and using that reading as the next sequence. 
    For example, 211 is read as "one two, two ones", 
    which becomes 1221 (1 2, 2 1s).

    Look-and-say sequences are generated iteratively, 
    using the previous value as input for the next step. 
    For each step, take the previous value, and replace each run of 
    digits (like 111) with the number of digits (3) 
    followed by the digit itself (1).

    For example:

    1 becomes 11 (1 copy of digit 1).
    11 becomes 21 (2 copies of digit 1).
    21 becomes 1211 (one 2 followed by one 1).
    1211 becomes 111221 (one 1, one 2, and two 1s).
    111221 becomes 312211 (three 1s, two 2s, and one 1).
    Starting with the digits in your puzzle input, apply 
    this process 40 times. 
    What is the length of the result?    
    '''
    print(f'{quiz_input = }')

    string= quiz_input
    for step in range(40):
        pos = count = 0
        sequence = []
        while pos <= (len(string) -1):
            char = string[pos]
            count += 1
            try:
                while string[pos+1] == char:
                    count += 1
                    pos += 1
            except IndexError:
                pass
            sequence.append((count, char))
            count = 0
            pos += 1
        
        string = [''.join(map(str, group)) for group in sequence]
        string = ''.join(string)
    return len(string)



if __name__ == '__main__':
    LOGFILE = str(Path(sys.argv[0]).parent / Path(__file__).stem) + '.log'
    handlers = [
        logging.FileHandler(LOGFILE, mode='w'),
        logging.StreamHandler()
    ]
    main.main(solution, input='1113222113', level='DEBUG', handlers=handlers)