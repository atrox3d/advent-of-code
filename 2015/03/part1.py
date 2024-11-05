from pathlib import Path
import sys
import pytest

def solve(quiz_input):
    r, c = 0, 0
    start = r, c
    path = set()
    path.add(start)
    for step in quiz_input:
        if step == '>':
            c += 1
        elif step == '<':
            c -= 1
        elif step == 'v':
            r += 1
        elif step == '^':
            r -= 1
        tile = r, c
        path.add(tile)
    return len(path)

def solution(input_path):
    with open(input_path) as fp:
        input_text = fp.read()

    return solve(input_text)

@pytest.mark.parametrize(
        'test, expected', [
            ('>', 2),
            ('^>v<', 4),
            ('^v^v^v^v^v', 2),
        ]
)
def test_solution_2015_03_1(test, expected):
    result = solve(test)
    assert result == expected

