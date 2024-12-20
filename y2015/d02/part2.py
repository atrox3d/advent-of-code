import sys
import pytest

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

def compute_ribbon(partials):    
    total = sum(partials)
    return total


def solution(input_path:str):
    '''called from aoc/main.py'''

    with open(input_path) as fp:
        lines = [line.rstrip() for line in fp.readlines()]
        boxes = [parse_box(line) for line in lines]
        int_boxes = [convert_box(box) for box in boxes]
        papers = [get_total_ribbon(l, w, h) for l, w, h in int_boxes]
        total = sum(papers)
        print(total)
        return total

@pytest.mark.parametrize(
        'box_str, expected', [
        ('2x3x4', (10, 24, 34)),
        ('1x1x10', (4, 10, 14))
    ]
)
def test_solution_2015_02_2(box_str, expected):
    box = parse_box(box_str)
    int_box = convert_box(box)
    partials = get_ribbon_and_slack(*int_box)
    result =  partials + (sum(partials), )
    assert result == expected


