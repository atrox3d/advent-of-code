from abc import ABC, abstractmethod
from copy import deepcopy

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

class Grid:
    ON = '#'
    OFF = '.'

    def __init__(self, grid_data:str, strategy:GridStrategy) -> None:
        self.strategy = strategy
        self.grid = strategy.parse_grid(grid_data)
    
    @classmethod
    def from_file(cls, path:str, strategy:GridStrategy):
        with open(path) as fp:
            grid_data = fp.read()
        return cls(grid_data, strategy)

    def width(self) -> int:
        return len(self.grid[0])

    def heigth(self) -> int:
        return len(self.grid)

    def check(self, row=None, col=None):
        if row is not None and (row < 0 or row >= self.heigth()):
            raise GridCoordError(f'invalid row {row}')
        if col is not None and (col < 0 or col >= self.width()):
            raise GridCoordError(f'invalid col {col}')

    # @checked
    def row(self, n:int) -> list:
        self.check(row=n)
        return self.grid[n]

    # @checked
    def col(self, n:int) -> list:
        self.check(col=n)
        return [row[n] for row in self.grid]
    
    # @checked
    def value(self, r, c) -> str:
        self.check(row=r, col=c)
        return self.grid[r][c]
    
    def print(self) -> None:
        for row in range(self.heigth()):
            for col in range(self.width()):
                print(self.value(row, col), end='')
            print()
    
    def neighbors(self, r, c) -> list[str]:
        upper_offests = [(-1, -1), (-1, 0), (-1, 1)]
        middle_offests = [(0, -1), (0, 1)]
        lower_offests = [(1, -1), (1, 0), (1, 1)]
        offsets = upper_offests + middle_offests + lower_offests

        values = []
        for offset in offsets:
            try:
                coords = tuple(map(sum, zip((r,c), offset)))
                value = self.value(*coords)
                values.append(value)
            except GridCoordError:
                # print(f'wrong coords {coords}')
                pass
        return values
    
    def state(self, r, c) -> int:
        values = [self.value(r, c), *self.neighbors(r, c)]
        return sum(1 if value==self.ON else 0 for value in values)
    
    def get(self, copy=False) -> list:
        if copy:
            return deepcopy(self.grid)
        else:
            return self.grid
    
    def update(self, grid:list, copy=False):
        if copy:
            self.grid = deepcopy(grid)
        else:
            self.grid = grid
    
    def load(self, path:str, strategy:GridStrategy):
        with open(path) as fp:
            grid_data = fp.read()
        self.grid = strategy.parse_grid(grid_data)


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent / 'test.txt'
    grid = Grid.from_file(path, LineStrategy())

    grid.print()
    print(grid.neighbors(5, 2))
    print(grid.state(5, 2))

    with open(path) as fp:
        grid = Grid(fp.read(), LineStrategy())

    grid.print()
    print(grid.neighbors(5, 2))
    print(grid.state(5, 2))
