from pathlib import Path
import sys
            
def solution(quiz_input):
    """
    Realizing the error of his ways, Santa has switched to a better model of determining 
    whether a string is naughty or nice. 
    None of the old rules apply, as they are all clearly ridiculous.

    Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice 
    in the string without overlapping, 
    like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    
    It contains at least one letter which repeats with exactly one letter between them, 
    like xyx, abcdefeghi (efe), or even aaa.
    For example:

    qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) 
    and a letter that repeats with exactly one letter between them (zxz).
    
    xxyxx is nice because it has a pair that appears twice 
    and a letter that repeats with one between, 
    even though the letters used by each rule overlap.
    
    uurcxstgmygtbstg is naughty because it has a pair (tg) 
    but no repeat with a single letter between them.
    
    ieodomkazucvgmuy is naughty because it has a repeating letter 
    with one between (odo), but no pair that appears twice.
    
    How many strings are nice under these new rules?
    """
    VOWELS = 'aeiou'
    FORBIDDEN = 'ab', 'cd', 'pq', 'xy'
    
    def has_three_vowels(word: str) -> bool:
        return len([v for v in word if v in VOWELS]) >= 3
    
    def twice_in_a_row(word: str) -> bool:
        for pos, char in enumerate(word):
            try:
                if char == word[pos+1]:
                    return True
            except IndexError:
                pass
        return False
    
    def allowed(word: str) -> bool:
        for forbidden in FORBIDDEN:
            if forbidden in word:
                return False
        return True

    def is_nice(word: str) -> bool:
        vowels_ok = has_three_vowels(word)
        print(f'{word} -> {vowels_ok = }')

        twice_ok = twice_in_a_row(word)
        print(f'{word} -> {twice_ok = }')

        allowed_ok = allowed(word)
        print(f'{word} -> {allowed_ok = }')

        return all([vowels_ok, twice_ok, allowed_ok])

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
                'input': ['qjhvhtzxzqqjkmpb'], 
                'expected': {'nice': 1, 'naughty': 0},
            },
            {
                'input': ['xxyxx'], 
                'expected': {'nice': 1, 'naughty': 0},
            },
            {
                'input': ['uurcxstgmygtbstg'], 
                'expected': {'nice': 0, 'naughty': 1},
            },
            {
                'input': ['ieodomkazucvgmuy'], 
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
                print('PASS')
            except AssertionError as ae:
                print(repr(ae))
            finally:
                print()
    else:
        print(solution(sys.argv[1:]))

else:
    with open(Path(__file__).parent / 'input.txt') as fp:
        quiz_input = [line.rstrip() for line in fp.readlines()]
        print(solution(quiz_input))
