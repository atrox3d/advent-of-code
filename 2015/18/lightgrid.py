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
        else:
            self.set(row, col, state)
        self.fixed[(row, col)] = state
    
    def is_fixed(self, row:int, col:int) -> bool:
        return (row, col) in self.fixed.keys()
    
    def set(self, r, c, value) -> str:
        if self.is_fixed(r, c):
            raise FixedLightError(f'light at {r,c} is fixed')
        return super().set(r, c, value)
    
    # def check_fixed(self, row:int, col:int) -> bool:
        # if self.is_fixed(row, col):


def step(grid:LightGrid,  printgrid=False, end='') -> 'LightGrid':
    '''
The state a light should have next is based on its current state (on or off) plus 
the number of neighbors that are on:

    - A light which is on stays on when 2 or 3 neighbors are on, 
        and turns off otherwise.

    - A light which is off turns on if exactly 3 neighbors are on, 
        and stays off otherwise.

    - All of the lights update simultaneously; 
        they all consider the same current state before moving to the next.

    '''
    # if printgrid:
        # grid.print(state=True, end=end)

    logger.info('copying grid')
    copy: LightGrid = grid.copy()

    logger.info('updating copy')
    for row, col, value in grid.foreach():
        state = grid.state(row, col)

        if value == LightGrid.ON:
            if not 2 <= state <= 3:
                copy.toggle(row, col)

        if value == LightGrid.OFF:
            if state == 3:
                copy.toggle(row, col)
    if printgrid:
        print()
        copy.print(state=True, end=end)
    
    logger.info('returning copy')
    return copy

# if __name__ == '__main__':
#     from pathlib import Path

#     path = Path(__file__).parent / 'test2.txt'
#     lg = LightGrid.from_file(path, CellStrategy())
#     lg.fix(0, 0, LightGrid.ON)
#     print(lg.is_fixed(0, 0))
#     lg.toggle(0, 0)

