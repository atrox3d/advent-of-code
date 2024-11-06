import pytest

# fix for vscode pytest
try:
    import common
except:
    from . import common

def solve(quiz_input:str, strategy):
    grid = [[0 for c in range(1000)] for r in range(1000)]
    for line in quiz_input:
        instruction = common.parse_instruction(line)
        common.act(grid, *instruction, strategy)
    result = sum([sum(r) for r in grid])
    print(result)
    return result

def solution(input_path):
    '''called from aoc/main.py'''

    with open(input_path) as fp:
        input_text = fp.readlines()
    
    return solve(input_text, common.strategy_part1)

@pytest.mark.parametrize(
        'instructions, expected', [
            (['turn on 0,0 through 999,999'], 1000000),
            (['toggle 0,0 through 999,0'], 1000),
            (['turn off 499,499 through 500,500'], 0),
        ]
)
def test_solution_2015_06_1(instructions, expected):
    '''
    turn on 0,0 through 999,999 
    would turn on (or leave on) every light.
    
    toggle 0,0 through 999,0
    would toggle the first line of 1000 lights, 
    turning off the ones that were on, and turning on the ones that were off.
    
    turn off 499,499 through 500,500
    would turn off (or leave off) the middle four lights.
    '''
    print(instructions[0])
    result = solve(instructions, common.strategy_part1)
    assert  result == expected


