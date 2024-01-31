from pathlib import Path
import sys
            
def solution(quiz_input):
    """
    """
    return quiz_input

if sys.argv[1:]:
    param = sys.argv[1]
    if param.lower() == 'test':
        tests = [
            {
                'input': '', 
                'expected': 0,
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
    with open(Path(__file__).with_suffix('.txt')) as fp:
        quiz_input = fp.read().rstrip()
        print(solution(quiz_input))
