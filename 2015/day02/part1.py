from pathlib import Path
import sys

def get_total_paper(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l + min(l, w, h)**2

def get_paper_and_slack(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l, min(l, w, h)**2

def convert_box(box):
    return tuple(map(int, box))

def parse_box(line):
    return line.rstrip().split('x')

def test_paper(box_str):
    print(f'{box_str = }')
    box = parse_box(box_str)
    print(f'{box = }')
    int_box = convert_box(box)
    print(f'{int_box = }')
    partials = get_paper_and_slack(*int_box)
    print(f'{partials = }')
    return partials + (sum(partials), )
    
def compute_paper(partials):    
    total = sum(partials)
    print(f'{total = }')
    return total


if sys.argv[1:]:
    param = sys.argv[1]
    if param.lower() == 'test':
        tests = {'2x3x4':(52, 6, 58), '1x1x10':(42, 1, 43)}
        for test, expected in tests.items():
            print(f'testing {test=}: {expected=}')
            result = test_paper(test)
            assert expected == result, f'{expected=} != {result=}'
    elif param.count('x') == 2:
        compute_paper(param)
    else:
        raise ValueError(f'wrong parameter format {param}')
else:
    with open(Path(__file__).with_suffix('.txt')) as fp:
        lines = [line.rstrip() for line in fp.readlines()]
        boxes = [parse_box(line) for line in lines]
        int_boxes = [convert_box(box) for box in boxes]
        papers = [get_total_paper(l, w, h) for l, w, h in int_boxes]
        for line, box, int_box, paper in zip(lines, boxes, int_boxes, papers):
            print(f'{line, box, int_box,  paper = }')
        total = sum(papers)
        print(total)

