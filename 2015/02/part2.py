from pathlib import Path
import sys

def get_bow(l, w, h):
    return l * w * h

def get_ribbon(l, w, h):
    a, b = sorted((l, w, h))[:2]
    return 2*a + 2 *b

def get_total_ribbon(l, w, h):
    return get_ribbon(l, w, h) + get_bow(l, w, h)

def get_ribbon_and_slack(l, w, h):
    return get_ribbon(l, w, h), get_bow(l, w, h)

def parse_box(line):
    return line.rstrip().split('x')

def convert_box(box):
    return tuple(map(int, box))

def test_ribbon(box_str):
    box = parse_box(box_str)
    int_box = convert_box(box)
    partials = get_ribbon_and_slack(*int_box)
    return partials + (sum(partials), )
    
def compute_ribbon(partials):    
    total = sum(partials)
    return total


if sys.argv[1:]:
    param = sys.argv[1]
    if param.lower() == 'test':
        tests = {
            '2x3x4':(10, 24, 34), 
            '1x1x10':(4, 10, 14)
        }
        for test, expected in tests.items():
            print(f'testing {test=}: {expected=}')
            result = test_ribbon(test)
            try:
                assert expected == result, f'{expected=} != {result=}'
            except AssertionError as ae:
                print(repr(ae))
    elif param.count('x') == 2:
        compute_ribbon(param)
    else:
        raise ValueError(f'wrong parameter format {param}')
else:
    with open(Path(__file__).with_suffix('.txt')) as fp:
        lines = [line.rstrip() for line in fp.readlines()]
        boxes = [parse_box(line) for line in lines]
        int_boxes = [convert_box(box) for box in boxes]
        papers = [get_total_ribbon(l, w, h) for l, w, h in int_boxes]
        total = sum(papers)
        print(total)

