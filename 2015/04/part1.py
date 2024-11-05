from pathlib import Path
import sys

import pytest
            
def solve(quiz_input):
    """
    Santa needs help mining some AdventCoins (very similar to bitcoins) 
    to use as gifts for all the economically forward-thinking 
    little girls and boys.

    To do this, he needs to find MD5 hashes which, in hexadecimal, 
    start with at least five zeroes. 
    The input to the MD5 hash is some secret key (your puzzle input, 
    given below) followed by a number in decimal. 
    To mine AdventCoins, you must find Santa the lowest positive 
    number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

    For example:

    If your secret key is 'abcdef', the answer is '609043', 
    because the MD5 hash of 'abcdef609043' starts with five zeroes 
    (000001dbbfa...), and it is the lowest such number to do so.
    
    If your secret key is 'pqrstuv', the lowest number it combines 
    with to make an MD5 hash starting with five zeroes is '1048970'; 
    that is, the MD5 hash of 'pqrstuv1048970' looks like (000006136ef....)
    
    Your puzzle input is ckczppom.
    """
    import hashlib

    number = 0
    while True:
        strng = f'{quiz_input}{number}'
        result = hashlib.md5(strng.encode()).hexdigest()
        if result.startswith('0' * 5):
            return number
        number += 1

def solution(input_path):
    with open(input_path) as fp:
        input_text = fp.read()

    return solve(input_text)

@pytest.mark.parametrize(
        'test, expected', [
            ('abcdef', 609043), 
            ('pqrstuv', 1048970)
        ]
)
def test_solution_2015_03_1(test, expected):
    result = solve(test)
    assert result == expected
