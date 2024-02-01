from pathlib import Path
import sys
            
def solution(quiz_input):
    """
    Realizing the error of his ways, Santa has switched to a better model of determining 
    whether a string is naughty or nice. 
    None of the old rules apply, as they are all clearly ridiculous.

    Now, a nice string is one with all of the following properties:

    - It contains a pair of any two letters that appears at least twice 
    in the string without overlapping, 
    like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    
    - It contains at least one letter which repeats with exactly one letter between them, 
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
    def get_groups(word: str, length) -> bool:
        pairs = [pair for pair in [word[pos:pos+length] for pos in range(len(word))] 
                 if len(pair) == length]
        return pairs

    def find_repeated_pairs(pairs: list[str], at_least):
        min_repeats = {pair:pairs.count(pair) for pair in pairs if pairs.count(pair) >= at_least}
        return min_repeats.keys()

    def at_least_twice(word: str) -> bool:
        pairs = get_groups(word, 2)
        return find_repeated_pairs(pairs, at_least=2)
        
    def non_overlapping(word: str, pairs: list[str]) -> list[str]:
        for pair in pairs:
            for pos in range(len(word)):
                if word[pos:].startswith(pair):
                    large = word[pos-1:pos+len(pair)+1]
                    # print(f'checking {pair}: {large=}')
                    try:
                        if large[0]==large[1] or large[-2]==large[-1]:
                            return False
                    except IndexError:
                        pass
        return True
    
    def in_between(word: str) -> bool:
        triplets = get_groups(word, 3)
        betweens = [triplet for triplet in triplets if triplet[0]==triplet[-1]]
        if len(betweens) > 0:
            # print(f'{betweens = }')
            return True
        return False

    def is_nice(word: str) -> bool:
        twice = at_least_twice(word)
        no_overlap = non_overlapping(word, twice)

        print(f'{word} -> {twice = }')
        print(f'{word} -> {no_overlap = }')

        between_ok = in_between(word)
        print(f'{word} -> {between_ok = }')

        return all([no_overlap, between_ok])

    nice = naughty = 0
    for word in quiz_input:
        if is_nice(word):
            nice += 1
        else:
            naughty += 1
        print()

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
                print(f'PASS {result =}')
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
