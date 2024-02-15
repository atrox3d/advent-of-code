"""
https://adventofcode.com/YEAR/day/DAY
https://adventofcode.com/YEAR/day/DAY#part2
"""
import logging
import sys, os
import re, json
from pathlib import Path

def update_syspath():
    cwd = Path.cwd()
    while cwd.name != 'aoc':
        cwd = cwd.parent
    print(cwd)
    sys.path.append(str(cwd))

update_syspath()
from aoclib import main

logger = logging.getLogger(__name__)
def solution(quiz_input):
    '''
    --- Day 11: Corporate Policy ---
    Santa's previous password expired, and he needs help choosing 
    a new one.

    To help him remember his new password after the old one expires, 
    Santa has devised a method of coming up with a password based on 
    the previous one. 
    Corporate policy dictates that passwords must be exactly 
    eight lowercase letters (for security reasons), 
    so he finds his new password by incrementing his old 
    password string repeatedly until it is valid.

    Incrementing is just like counting with numbers: 
    xx, xy, xz, ya, yb, and so on. 
    Increase the rightmost letter one step; 
    if it was z, it wraps around to a, and repeat with the 
    next letter to the left until one doesn't wrap around.

    Unfortunately for Santa, a new Security-Elf recently started, 
    and he has imposed some additional password requirements:

    -   Passwords must include one increasing straight of at least 
        three letters, like abc, bcd, cde, and so on, up to xyz. 
        They cannot skip letters; abd doesn't count.
    
    -   Passwords may not contain the letters i, o, or l, 
        as these letters can be mistaken for other characters and 
        are therefore confusing.
    
    -   Passwords must contain at least two different, 
        non-overlapping pairs of letters, like aa, bb, or zz.
    
    For example:

    hijklmmn meets the first requirement (because it contains the 
    straight hij) but fails the second requirement requirement 
    (because it contains i and l).
    
    abbceffg meets the third requirement (because it repeats bb and ff) 
    but fails the first requirement.
    
    abbcegjk fails the third requirement, because it only has one 
    double letter (bb).
    
    -> The next password after abcdefgh is abcdffaa.

    -> The next password after ghijklmn is ghjaabcc, 
    because you eventually skip all the passwords that start with 
    ghi..., since i is not allowed.
    
    Given Santa's current password (your puzzle input), 
    what should his next password be?

    Your puzzle input is cqjxjnds. cqjxkkaa   
    '''
    from increment import increment
    from rincrement import rincrement
    from valid import is_valid, valid_chars

    result = quiz_input
    # result = 'ghizzzzz'
    logger.debug(f'{result = }')
    while not is_valid(result):
        if result == 'ghjaabcc':
            print(f'{quiz_input = } {result = }')
            input('ERROR')

        # os.system('clear')
        # logger.debug(f'{result = }')
        result = rincrement(result, valid_chars)
        # print(f'{quiz_input = }, {result = }')
        # if result.startswith('ghia'):
            # logger.info(f'{result = }')
    return result

if __name__ == '__main__':
    LOGFILE = str(Path(sys.argv[0]).parent / Path(__file__).stem) + '.log'
    handlers = [
        logging.FileHandler(LOGFILE, mode='w'), 
        logging.StreamHandler()
        ]

    for test_input, test_expected in (
        ('abcdefgh', 'abcdffaa'),
        ('ghijklmn', 'ghjaabcc'),
        ('cqjxjnds', 'boh'),
    ):
        main.main(
                    solution, 
                    input=None,
                    test_input=test_input,
                    test_expected=test_expected, 
                    level='INFO', 
                    handlers=handlers
                )