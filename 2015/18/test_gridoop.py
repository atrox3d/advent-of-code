from pathlib import Path
import pytest 

try:
    import gridoop as goop
except:
    from . import gridoop as goop

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

def test_grid_from_file_line_strategy(test_file1, grid_line1):
    grid = goop.Grid.from_file(test_file1, goop.LineStrategy())
    assert grid_line1 == grid.get_grid()

def test_grid_from_file_cell_strategy(test_file1, grid_cell1):
    grid = goop.Grid.from_file(test_file1, goop.CellStrategy())
    assert grid_cell1 == grid.get_grid()

def test_grid_line_strategy(quiz_input1, grid_line1):
    grid = goop.Grid(quiz_input1, goop.LineStrategy())
    assert grid_line1 == grid.get_grid()

def test_grid_cell_strategy(quiz_input1, grid_cell1):
    grid = goop.Grid(quiz_input1, goop.CellStrategy())
    assert grid_cell1 == grid.get_grid()

def test_grid_width_line(quiz_input1, grid_line1):
    grid = goop.Grid(quiz_input1, goop.LineStrategy())
    assert grid.width() == len(grid_line1[0])

def test_grid_width_cell(quiz_input1, grid_cell1):
    grid = goop.Grid(quiz_input1, goop.CellStrategy())
    assert grid.width() == len(grid_cell1[0])

def test_grid_height_line(quiz_input1, grid_line1):
    grid = goop.Grid(quiz_input1, goop.LineStrategy())
    assert grid.heigth() == len(grid_line1)

def test_grid_height_cell(quiz_input1, grid_cell1):
    grid = goop.Grid(quiz_input1, goop.CellStrategy())
    assert grid.heigth() == len(grid_cell1)

def test_check(quiz_input1):
    grid = goop.Grid(quiz_input1, goop.CellStrategy())
    grid.check(0, 0)
    with pytest.raises(goop.GridCoordError):
        grid.check(grid.heigth() +1, 0)
    with pytest.raises(goop.GridCoordError):
        grid.check(0, grid.width() +1)

def test_row(quiz_input1, grid_line1, grid_cell1):
    grid = goop.Grid(quiz_input1, goop.LineStrategy())
    assert grid_line1[0] == grid.row(0)

    with pytest.raises(goop.GridCoordError):
        grid.row(1000)

    grid = goop.Grid(quiz_input1, goop.CellStrategy())
    assert grid_cell1[0] == grid.row(0)

    with pytest.raises(goop.GridCoordError):
        grid.row(1000)

def test_col(quiz_input1, grid_line1, grid_cell1):
    grid = goop.Grid(quiz_input1, goop.LineStrategy())
    assert [row[0] for row in grid_line1] == grid.col(0)

    with pytest.raises(goop.GridCoordError):
        grid.col(1000)

    grid = goop.Grid(quiz_input1, goop.CellStrategy())
    assert [row[0] for row in grid_cell1] == grid.col(0)

    with pytest.raises(goop.GridCoordError):
        grid.col(1000)

def test_get(quiz_input1, grid_line1, grid_cell1):
    grid = goop.Grid(quiz_input1, goop.LineStrategy())
    for y in range(grid.heigth()):
        for x in range(grid.width()):
            assert grid_line1[y][x] == grid.get(y, x)

    with pytest.raises(goop.GridCoordError):
        grid.get(1000, 1000)    
    
    grid = goop.Grid(quiz_input1, goop.CellStrategy())
    for y in range(grid.heigth()):
        for x in range(grid.width()):
            assert grid_cell1[y][x] == grid.get(y, x)

    with pytest.raises(goop.GridCoordError):
        grid.get(1000, 1000)    

def test_set(quiz_input1, grid_line1, grid_cell1):
    grid = goop.Grid(quiz_input1, goop.LineStrategy())
    grid.set(0, 0, '#')
    assert grid.get(0, 0) == '#'

    with pytest.raises(goop.GridCoordError):
        grid.set(1000, 1000, '#')

    with pytest.raises(goop.GridValueError):
        grid.set(0, 0, 'A')

    grid = goop.Grid(quiz_input1, goop.CellStrategy())
    grid.set(0, 0, '#')
    assert grid.get(0, 0) == '#'

    with pytest.raises(goop.GridCoordError):
        grid.set(1000, 1000, '#')

    with pytest.raises(goop.GridValueError):
        grid.set(0, 0, 'A')

def test_neighbors(quiz_input1, grid_cell1, grid_line1):
    grid = goop.Grid(quiz_input1, goop.LineStrategy())
    assert grid.neighbors(0, 0) == ['#', '.', '.']

    grid = goop.Grid(quiz_input1, goop.CellStrategy())
    assert grid.neighbors(0, 0) == ['#', '.', '.']

def test_state(quiz_input1):
    grid = goop.Grid(quiz_input1, goop.LineStrategy())
    assert grid.state(0, 0) == 1
    assert grid.state(0, 1) == 0

    grid = goop.Grid(quiz_input1, goop.CellStrategy())
    assert grid.state(0, 0) == 1
    assert grid.state(0, 1) == 0

def test_update(quiz_input1, quiz_input2):
    grid1 = goop.Grid(quiz_input1, goop.LineStrategy())
    grid2 = goop.Grid(quiz_input2, goop.LineStrategy())
    grid1.update(grid2)
    assert grid1.get_grid() == grid2.get_grid()

    grid1 = goop.Grid(quiz_input1, goop.CellStrategy())
    grid2 = goop.Grid(quiz_input2, goop.CellStrategy())
    grid1.update(grid2)
    assert grid1.get_grid() == grid2.get_grid()

def test_foreach(quiz_input1, grid_line1, grid_cell1):
    grid1 = goop.Grid(quiz_input1, goop.LineStrategy())
    grid2 = goop.Grid(quiz_input1, goop.CellStrategy())
    
    for (ya, yb, a), (yb, xb, b), c, d in zip(
            grid1.foreach(), 
            grid2.foreach(),
            (c for row in grid_line1 for c in row),
            (c for row in grid_cell1 for c in row)
        ):
        assert a == b == c == d

