from pathlib import Path
import sys
            
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

    def is_nice(word: str) -> bool:
        three_vowels = re.match(r'[aeiou]{3,}', word)
        print(f'{word = }, {three_vowels = }')

        double = re.match(r'(.)\1', word)
        print(f'{word = }, {double = }')

        exclude = re.match(r'^((?!ab|cd|pq|xy).)*$', word)
        print(f'{word = }, {exclude = }')

        result = three_vowels is not None \
                and double is not None \
                and exclude is not None
        print(f'{result = }')
        return result
    
    nice = naughty = 0
    for word in quiz_input:
        if is_nice(word):
            nice += 1
        else:
            naughty += 1

    return dict(nice=nice, naughty=naughty)

if sys.argv[1:]:
    param = sys.argv[1]
    if param.lower() == 'test':
        tests = [
            {
                'input': ['aaa'], 
                'expected': {'nice': 1, 'naughty': 0},
            },
            {
                'input': ['jchzalrnumimnmhp'], 
                'expected': {'nice': 0, 'naughty': 1},
            },
            {
                'input': ['dvszwmarrgswjxmb'], 
                'expected': {'nice': 0, 'naughty': 1},
            },
        ]
        for test in tests:
            _input = test['input']
            expected = test['expected']
            print(f'testing {_input}: {expected=}')
            result = solution(test['input'])
            try:
                assert expected == result, f'{expected=} != {result=}'
                print(f'PASS: {expected=} != {result=}')
            except AssertionError as ae:
                print(f'FAIL: {expected=} != {result=}')
                # print(repr(ae))
            finally:
                print()
    else:
        print(solution(sys.argv[1:]))

else:
    with open(Path(__file__).parent / 'input.txt') as fp:
        quiz_input = [line.rstrip() for line in fp.readlines()]
        print(solution(quiz_input))
