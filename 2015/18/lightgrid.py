import logging

from gridoop import (
        Grid, 
        GridStrategy, LineStrategy, CellStrategy, 
        GridValueError, GridCoordError,
    )

logger = logging.getLogger(__name__)

class FixedLightError(ValueError): pass

class LightGrid(Grid):

    def __init__(self, grid_data: str, strategy: GridStrategy) -> None:
        super().__init__(grid_data, strategy)
        self.fixed = {}
    
    def turnon(self, row:int, col:int) -> None:
        try:
            self.set(row, col, self.ON)
        except FixedLightError as fle:
            logger.warning(fle)

    def turnoff(self, row:int, col:int) -> None:
        try:
            self.set(row, col, self.OFF)
        except FixedLightError as fle:
            logger.warning(fle)

    def toggle(self, row:int, col:int) -> None:
        try:
            if self.get(row, col) == self.ON:
                self.set(row, col, self.OFF)
            elif self.get(row, col) == self.OFF:
                self.set(row, col, self.ON)
            else:
                value = self.get(row, col)
                raise GridValueError(f'invalid value {value} at {row, col}')
        except FixedLightError as fle:
            logger.warning(fle)

    def fix(self, row:int, col:int, state:str=None):
        if state is None:
            state = self.get(row, col)
        self.fixed[(row, col)] = state
    
    def is_fixed(self, row:int, col:int) -> bool:
        return (row, col) in self.fixed.keys()
    
    def set(self, r, c, value) -> str:
        if self.is_fixed(r, c):
            raise FixedLightError(f'light at {r,c} is fixed')
        return super().set(r, c, value)
    
    # def check_fixed(self, row:int, col:int) -> bool:
        # if self.is_fixed(row, col):



if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent / 'test2.txt'
    lg = LightGrid.from_file(path, CellStrategy())
    lg.fix(0, 0, LightGrid.ON)
    print(lg.is_fixed(0, 0))
    lg.toggle(0, 0)

