from pathlib import Path
import pytest 

try:
    import lightgrid as lg
except:
    from . import lightgrid as lg

@pytest.fixture
def test_file1():
    test_file = Path(__file__).parent / 'test1.txt'
    return test_file

@pytest.fixture
def quiz_input1(test_file1) -> str:
    with open(test_file1, 'r') as fp:
        return fp.read()

@pytest.fixture
def test_file2():
    test_file = Path(__file__).parent / 'test2.txt'
    return test_file

@pytest.fixture
def quiz_input2(test_file2) -> str:
    with open(test_file2, 'r') as fp:
        return fp.read()

@pytest.fixture
def grid_line1():
    return [
        '.#.#.#', 
        '...##.', 
        '#....#', 
        '..#...', 
        '#.#..#', 
        '####..'
    ]

@pytest.fixture
def grid_line2():
    return [
        '##.#.#', 
        '...##.', 
        '#....#', 
        '..#...', 
        '#.#..#', 
        '####.#'
    ]

@pytest.fixture
def grid_cell1():
    return [
        ['.', '#', '.', '#', '.', '#'], 
        ['.', '.', '.', '#', '#', '.'], 
        ['#', '.', '.', '.', '.', '#'], 
        ['.', '.', '#', '.', '.', '.'], 
        ['#', '.', '#', '.', '.', '#'], 
        ['#', '#', '#', '#', '.', '.']
        ]

@pytest.fixture
def grid_cell2():
    return [
        ['#', '#', '.', '#', '.', '#'], 
        ['.', '.', '.', '#', '#', '.'], 
        ['#', '.', '.', '.', '.', '#'], 
        ['.', '.', '#', '.', '.', '.'], 
        ['#', '.', '#', '.', '.', '#'], 
        ['#', '#', '#', '#', '.', '#']
        ]

def test_lightgrid(test_file1, grid_cell1, grid_line1):
    linegrid = lg.LightGrid.from_file(test_file1, lg.LineStrategy())
    linegrid.print()
    assert grid_line1 == linegrid.get_grid()

    cellgrid = lg.LightGrid.from_file(test_file1, lg.CellStrategy())
    cellgrid.print()
    assert grid_cell1 == cellgrid.get_grid()

def test_turnon(quiz_input1):
    linegrid = lg.LightGrid(quiz_input1, lg.LineStrategy())
    linegrid.turnon(0, 0)
    assert linegrid.get(0, 0) == linegrid.ON

    cellgrid = lg.LightGrid(quiz_input1, lg.CellStrategy())
    cellgrid.turnon(0, 0)
    assert cellgrid.get(0, 0) == linegrid.ON

def test_turnoff(quiz_input1):
    linegrid = lg.LightGrid(quiz_input1, lg.LineStrategy())
    linegrid.turnoff(0, 0)
    assert linegrid.get(0, 0) == linegrid.OFF

    cellgrid = lg.LightGrid(quiz_input1, lg.CellStrategy())
    cellgrid.turnoff(0, 0)
    assert cellgrid.get(0, 0) == linegrid.OFF

def test_toggle(quiz_input1):
    linegrid = lg.LightGrid(quiz_input1, lg.LineStrategy())
    value = linegrid.get(0, 0)
    linegrid.toggle(0, 0)
    assert linegrid.get(0, 0) != value

    cellgrid = lg.LightGrid(quiz_input1, lg.CellStrategy())
    value = cellgrid.get(0, 0)
    cellgrid.toggle(0, 0)
    assert cellgrid.get(0, 0) != value

def test_is_fixed(quiz_input1):
    linegrid = lg.LightGrid(quiz_input1, lg.LineStrategy())
    assert linegrid.is_fixed(0, 0) == False
    linegrid.fix(0, 0)
    assert linegrid.is_fixed(0, 0) == True

    cellgrid = lg.LightGrid(quiz_input1, lg.CellStrategy())
    assert cellgrid.is_fixed(0, 0) == False
    cellgrid.fix(0, 0)
    assert cellgrid.is_fixed(0, 0) == True

def test_fixedlighterror(quiz_input1):
    linegrid = lg.LightGrid(quiz_input1, lg.LineStrategy())
    linegrid.fix(0, 0)
    with pytest.raises(lg.FixedLightError):
        linegrid.set(0, 0, linegrid.ON)

    with pytest.raises(lg.FixedLightError):
        linegrid.set(0, 0, linegrid.OFF)

    cellgrid = lg.LightGrid(quiz_input1, lg.CellStrategy())
    cellgrid.fix(0, 0)
    with pytest.raises(lg.FixedLightError):
        cellgrid.set(0, 0, cellgrid.ON)

    with pytest.raises(lg.FixedLightError):
        cellgrid.set(0, 0, cellgrid.OFF)




