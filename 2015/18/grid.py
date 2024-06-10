ON = '#'
OFF = '.'

def get_grid(puzzle_input:str) -> list[str]:
    grid = []
    for line in puzzle_input.splitlines():
        grid.append(line)
    return grid

def load_grid(path:str, gridfn=get_grid) -> list[str]:
    with open(path) as fp:
        grid_data = fp.read()
    return gridfn(grid_data)



