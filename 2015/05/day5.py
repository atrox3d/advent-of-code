import logging
import sys, os

sys.path.append(os.getcwd())
from aoclib import main

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
    import re

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
    
    nice = naughty = 0
    for word in quiz_input:
        if is_nice2(word):
            nice += 1
        else:
            naughty += 1

    return dict(nice=nice, naughty=naughty)


if __name__ == '__main__':
    main.main(solution, level='DEBUG')
