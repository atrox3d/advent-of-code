from pathlib import Path
import pytest

try:
    import grid
except:
    from . import grid


@pytest.fixture
def test_file():
    test_file = Path(__file__).parent / 'test1.txt'
    return test_file

@pytest.fixture
def quiz_input1(test_file) -> str:
    with open(test_file, 'r') as fp:
        return fp.read()

@pytest.fixture
def gridtest1():
    return [
        '.#.#.#', 
        '...##.', 
        '#....#', 
        '..#...', 
        '#.#..#', 
        '####..'
    ]

def test_get_from_string(quiz_input1, gridtest1):
    _grid = grid.get_from_string(quiz_input1)
    assert gridtest1 == _grid

def test_load_from_file(test_file, gridtest1):
    _grid = grid.load_from_file(test_file)
    assert gridtest1 == _grid

def test_get_value(gridtest1):
    for y, row in enumerate(gridtest1):
        for x, col in enumerate(row):
            assert gridtest1[y][x] == grid.get_value(gridtest1, y, x)

def test_get_width(gridtest1):
    assert len(gridtest1) == grid.get_width(gridtest1)

def test_get_row(gridtest1):
    assert gridtest1[0] == grid.get_row(gridtest1, 0)
    with pytest.raises(grid.GridRowException):
        grid.get_row(gridtest1, len(gridtest1) + 1)
    
def test_get_col(gridtest1):
    assert gridtest1[0][0] == grid.get_col(gridtest1[0], 0)
    with pytest.raises(grid.GridColException):
        grid.get_col(gridtest1[0], len(gridtest1[0]) + 1)
    

