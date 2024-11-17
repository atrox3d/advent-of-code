ON = '#'
OFF = '.'

class GridRowException(Exception): pass
class GridColException(Exception): pass

def get_from_string(puzzle_input:str) -> list[str]:
    grid = []
    for line in puzzle_input.splitlines():
        grid.append(line)
    return grid

def load_from_file(path:str, gridfn=get_from_string) -> list[str]:
    with open(path) as fp:
        grid_data = fp.read()
    return gridfn(grid_data)

def get_value(grid:list[str], r:int, c:int) -> str:
    row = get_row(grid, r)
    return get_col(row, c)


def get_width(grid:list[str]) -> int:
    return len(grid[0])

def get_heigth(grid:list[str]) -> int:
    return len(grid)

def get_row(grid:list[str], r) -> str:
    try:
        return grid[r]
    except IndexError as ie:
        grid_heigth = get_heigth(grid)
        raise GridRowException(f'row {r} not valid for grid heigth {grid_heigth}')

def get_col(grid_row:str, c) -> str:
    try:
        return grid_row[c]
    except IndexError as ie:
        grid_width = len(grid_row)
        raise GridColException(f'col {c} not valid for grid width {grid_width}')

# if __name__ == '__main__':
#     from pathlib import Path

#     grid = load_from_file(Path(__file__).parent / 'test.txt')
#     for r in range(get_heigth(grid)):
#         for c in range(get_width(grid)):
#             print(get_value(grid, r, c))

