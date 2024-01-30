from pathlib import Path
import sys


def solution():
    ...

if sys.argv[1:]:
    param = sys.argv[1]
    if param.lower() == 'test':
        tests = {
            'value':'expected',
            'value':'expected',
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
        ...
