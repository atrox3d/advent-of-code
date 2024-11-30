import logging
import sys, os
import re

import pytest


logger = logging.getLogger(__name__)
            
def solution(quiz_input):
    """
    Santa needs help figuring out which strings in his text file are 
    naughty or nice.

    A nice string is one with all of the following properties:

    - It contains at least three vowels (aeiou only), like aei, 
    xazegov, or aeiouaeiouaeiou.

    - It contains at least one letter that appears twice in a row, 
    like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).

    - It does not contain the strings ab, cd, pq, or xy, even 
    if they are part of one of the other requirements.
    
    For example:

    ugknbfddgicrmopn is nice because it has at least three 
    vowels (u...i...o...), a double letter (...dd...), 
    and none of the disallowed substrings.

    aaa is nice because it has at least three vowels and a 
    double letter, even though the letters used by different rules 
    overlap.

    jchzalrnumimnmhp is naughty because it has no double letter.

    haegwjzuvuyypxyu is naughty because it contains the string xy.

    dvszwmarrgswjxmb is naughty because it contains only one vowel.

    How many strings are nice?
    """

    # vowels = re.compile(r'[aeiou]{3,}')
    # repeat = re.compile(r'(.)\1')
    # exclude = re.compile(r'^((?!ab|cd|pq|xy).)*$')

def is_nice1(word: str) -> bool:
    three_vowels = re.findall(r'[aeiou]', word)
    three_vowels_ok = len(three_vowels) >= 3
    print(f'{word = }, {three_vowels = }, {three_vowels_ok = }')

    double = re.findall(r'(.)\1', word)
    double_ok = double != []
    print(f'{word = }, {double = }, {double_ok = }')

    exclude = re.match(r'^((?!ab|cd|pq|xy).)*$', word)
    exclude_ok = exclude is not None
    print(f'{word = }, {exclude = }, {exclude_ok = }')

    result = three_vowels_ok and double_ok and exclude_ok 
    print(f'{result = }')
    return result

def is_nice2(word: str) -> bool:
    logger.debug(f'{word=}')
    twice = re.search(r'(..).*\1', word)
    twice = twice is not None
    print(f'{word = }, {twice = }')

    between = re.search(r'(.).\1', word)
    between = between is not None
    print(f'{word = }, {between = }')

    return twice and between

def solve(quiz_input, isnice):
    nice = naughty = 0
    for word in quiz_input:
        if isnice(word):
            nice += 1
        else:
            naughty += 1

    return dict(nice=nice, naughty=naughty)

def solution(input_path):
    '''called from aoc/main.py'''

    with open(input_path) as fp:
        input_text = fp.readlines()
    
    print(solve(input_text, is_nice1))


@pytest.mark.parametrize(
        'word, isnice', [
            ('ugknbfddgicrmopn', True),
            ('aaa', True),
            ('jchzalrnumimnmhp', False),
            ('haegwjzuvuyypxyu', False),
            ('dvszwmarrgswjxmb', False),
        ]
)
def test_solution_2015_05_1(word, isnice):
    '''
    ugknbfddgicrmopn is nice because it has at least three 
    vowels (u...i...o...), a double letter (...dd...), 
    and none of the disallowed substrings.

    aaa is nice because it has at least three vowels and a 
    double letter, even though the letters used by different rules 
    overlap.

    jchzalrnumimnmhp is naughty because it has no double letter.

    haegwjzuvuyypxyu is naughty because it contains the string xy.

    dvszwmarrgswjxmb is naughty because it contains only one vowel.
    '''
    assert is_nice1(word) == isnice
