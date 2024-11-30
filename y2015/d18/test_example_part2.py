from pathlib import Path
import pytest 

try:
    import lightgrid as lg
except:
    from . import lightgrid as lg

@pytest.fixture
def example_file1() -> str:
    test_file = Path(__file__).parent / 'example2.txt'
    return test_file

@pytest.fixture
def steps_line(example_file1) -> list[lg.LightGrid]:
    with open(example_file1, 'r') as fp:
        lines = fp.read()
    
    blocks = lines.split('\n\n')

    steps = [lg.LightGrid(data, lg.LineStrategy()) for data in blocks]
    return steps

@pytest.fixture
def steps_cell(example_file1) -> list[lg.LightGrid]:
    with open(example_file1, 'r') as fp:
        lines = fp.read()
    
    blocks = lines.split('\n\n')

    steps = [lg.LightGrid(data, lg.CellStrategy()) for data in blocks]
    return steps

def test_fixed_line(steps_line):
    grid = lg.fix_corners(steps_line[0])

    top_left = 0, 0
    top_right = 0, grid.width() -1
    bottom_left = grid.heigth() -1, 0
    bottom_right = grid.heigth() -1, grid.width() -1

    assert grid.is_fixed(*top_left), f'{top_left} is not fixed'
    assert grid.is_fixed(*top_right), f'{top_right} is not fixed'
    assert grid.is_fixed(*bottom_left), f'{bottom_left} is not fixed'
    assert grid.is_fixed(*bottom_right), f'{bottom_right} is not fixed'

def test_steps_line(steps_line:list[lg.LightGrid]):
    step0 = lg.fix_corners(steps_line[0])
    step1 = lg.step(step0)
    assert step1 == steps_line[1]

    step2 = lg.step(step1)
    assert step2 == steps_line[2]

    step3 = lg.step(step2)
    assert step3 == steps_line[3]

    step4 = lg.step(step3)
    assert step4 == steps_line[4]

def test_steps_cell(steps_cell:list[lg.LightGrid]):
    step0 = lg.fix_corners(steps_cell[0])
    step1 = lg.step(step0)
    assert step1 == steps_cell[1]

    step2 = lg.step(step1)
    assert step2 == steps_cell[2]

    step3 = lg.step(step2)
    assert step3 == steps_cell[3]

    step4 = lg.step(step3)
    assert step4 == steps_cell[4]

