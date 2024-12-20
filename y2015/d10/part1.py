"""
https://adventofcode.com/2015/day/10
https://adventofcode.com/2015/day/10#part2
"""
import logging
import sys, os
import re, json
from pathlib import Path

# sys.path.append(os.getcwd())
# from aoclib import main

logger = logging.getLogger(__name__)

def solve(quiz_input):
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
    What is the length of the result? 252594
    '''
    print(f'{quiz_input = }')

    def look_and_say(string: str, reps: int) -> int:
        for _ in range(reps):
            prev_char = ''
            count = 0
            result = ''
            for char in string:
                if char != prev_char:
                    if prev_char != '':
                        result += f'{count}{prev_char}'
                        count = 0
                count += 1
                prev_char = char
            result += f'{count}{char}'
            string = result
            print(f'{_}: {len(result)}')

        return len(result)

    # return [look_and_say(quiz_input, reps) for reps in (40, 50)]
    return look_and_say(quiz_input, 40)

def solution(input_path):
    '''called from aoc/main.py'''

    print(f'open {input_path}')
    with open(input_path) as fp:
        input_text = fp.read()
    
    print(f'call solve <input_text>')
    result = solve(input_text)
    print(f'{result = }')
    print(f'end solution')


# if __name__ == '__main__':
#     LOGFILE = str(Path(sys.argv[0]).parent / Path(__file__).stem) + '.log'
#     handlers = [
#         logging.FileHandler(LOGFILE, mode='w'),
#         logging.StreamHandler()
#     ]
#     main.main(solution, input_param='1113222113', level='DEBUG', handlers=handlers)   