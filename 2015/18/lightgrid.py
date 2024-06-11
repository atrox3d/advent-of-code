from gridoop import (
        Grid, 
        GridStrategy, LineStrategy, CellStrategy, 
        GridValueError, GridCoordError,
    )

class LightGrid(Grid):

    def turnon(self, row:int, col:int) -> None:
        self.set(row, col, self.ON)

    def turnoff(self, row:int, col:int) -> None:
        self.set(row, col, self.OFF)

    def toggle(self, row:int, col:int) -> None:
        if self.get(row, col) == self.ON:
            self.set(row, col, self.OFF)
        elif self.get(row, col) == self.OFF:
            self.set(row, col, self.ON)
        else:
            value = self.get(row, col)
            raise GridValueError(f'invalid value {value} at {row, col}')


