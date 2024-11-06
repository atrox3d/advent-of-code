import pytest


def get_slack(l, w, h):
    a, b = sorted([l, w, h])[:2]
    return a*b

def get_total_paper(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l + get_slack(l, w, h)

def get_paper_and_slack(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l, get_slack(l, w, h)

def convert_box(box):
    return tuple(map(int, box))

def parse_box(line):
    return line.rstrip().split('x')
    
def compute_paper(partials):    
    total = sum(partials)
    return total

def solution(input_path:str):
    '''called from aoc/main.py'''

    with open(input_path) as fp:
        lines = [line.rstrip() for line in fp.readlines()]
        boxes = [parse_box(line) for line in lines]
        int_boxes = [convert_box(box) for box in boxes]
        papers = [get_total_paper(l, w, h) for l, w, h in int_boxes]
        total = sum(papers)
        print(total)
        return total

@pytest.mark.parametrize(
    'box_str, expected', [
    ('2x3x4', (52, 6, 58)), 
    ('1x1x10', (42, 1, 43))]
)
def test_solution_2015_02_1(box_str, expected):
    box = parse_box(box_str)
    int_box = convert_box(box)
    partials = get_paper_and_slack(*int_box)
    result = partials + (sum(partials), )
    assert result == expected

