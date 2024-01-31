from pathlib import Path
import sys

def get_pos(step, r, c):
    if step == '>':
        c += 1
    elif step == '<':
        c -= 1
    elif step == 'v':
        r += 1
    elif step == '^':
        r -= 1
    return r, c

def solution(quiz_input):
    r, c = 0, 0
    start = r, c
    path = set()
    path.add(start)
    for step in quiz_input[::2]:
        r, c = santatile = get_pos(step, r, c)
        path.add(santatile)

    r, c = 0, 0
    start = r, c
    for robostep in quiz_input[1::2]:
        r, c = robotile = get_pos(robostep, r, c)
        path.add(robotile)

    return len(path)

if sys.argv[1:]:
    param = sys.argv[1]
    if param.lower() == 'test':
        tests = {
            '^v': 3,
            '^>v<': 3,
            '^v^v^v^v^v': 11,
        }
        for test, expected in tests.items():
            print(f'testing {test=}: {expected=}')
            result = solution(test)
            try:
                assert expected == result, f'{expected=} != {result=}'
                print('PASS')
            except AssertionError as ae:
                print(repr(ae))
            finally:
                print()
else:
    with open(Path(__file__).with_suffix('.txt')) as fp:
        quiz_input = fp.read()
        print(solution(quiz_input))
