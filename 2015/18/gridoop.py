from abc import ABC, abstractmethod

class GridStrategy(ABC):

    @abstractmethod
    def parse_grid(self, grid_data:str) -> list:
        pass

class LineStrategy(GridStrategy):
    def parse_grid(self, grid_data: str) -> list[str]:
        grid = []
        for line in grid_data.splitlines():
            grid.append(line)
        return grid

class CellStrategy(GridStrategy):
    def parse_grid(self, grid_data: str) -> list[str]:
        grid = []
        for line in grid_data.splitlines():
            row = []
            for ch in line:
                row.append(ch)
            grid.append(row)
        return grid

class GridCoordError(Exception): pass

def checked(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except IndexError as ie:
            raise GridCoordError(f'invalid grid coordinates')
    return wrapper

class Grid:
    ON = '#'
    OFF = '.'

    def __init__(self, path:str, strategy:GridStrategy) -> None:
        self.path = path
        self.grid = []
        self.strategy = strategy
        self.load()

    def load(self, strategy=None) -> None:
        with open(self.path) as fp:
            grid_data = fp.read()
        strategy = strategy or self.strategy
        self.grid = strategy.parse_grid(grid_data)
    
    def width(self) -> int:
        return len(self.grid[0])

    def heigth(self) -> int:
        return len(self.grid)

    @checked
    def row(self, n:int) -> list:
        return self.grid[n]

    @checked
    def col(self, n:int) -> list:
        return [row[n] for row in self.grid]
    
    @checked
    def value(self, r, c) -> str:
        return self.grid[r][c]
    

if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent / 'test.txt'
    grid = Grid(path, LineStrategy())
    print(grid.value(5, 3))
