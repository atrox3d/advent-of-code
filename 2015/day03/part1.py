from pathlib import Path
import sys


def solution(quiz_input):
    print(quiz_input)

if sys.argv[1:]:
    param = sys.argv[1]
    if param.lower() == 'test':
        tests = {
            '>': 2,
            '^>v<': 4,
            '^v^v^v^v^v': 2,
        }
        for test, expected in tests.items():
            print(f'testing {test=}: {expected=}')
            result = solution(test)
            try:
                assert expected == result, f'{expected=} != {result=}'
            except AssertionError as ae:
                print(repr(ae))
else:
    with open(Path(__file__).with_suffix('.txt')) as fp:
        quiz_input = fp.read()
        print(solution(quiz_input))
