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

class Grid:

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

if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent / 'test.txt'
    grid = Grid(path, LineStrategy())
    print(grid.grid)
