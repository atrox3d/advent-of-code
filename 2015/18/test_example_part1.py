from pathlib import Path
import pytest 

try:
    import lightgrid as lg
except:
    from . import lightgrid as lg

@pytest.fixture
def example_file1() -> str:
    test_file = Path(__file__).parent / 'example1.txt'
    return test_file

@pytest.fixture
def steps_line(example_file1) -> list[lg.LightGrid]:
    with open(example_file1, 'r') as fp:
        lines = fp.read()
    
    blocks = lines.split('\n\n')

    steps = [lg.LightGrid(data, lg.LineStrategy()) for data in blocks]
    return steps

@pytest.fixture
def steps_cell(example_file1) -> list[lg.LightGrid]:
    with open(example_file1, 'r') as fp:
        lines = fp.read()
    
    blocks = lines.split('\n\n')

    steps = [lg.LightGrid(data, lg.CellStrategy()) for data in blocks]
    return steps

def test_steps(steps_line:list[lg.LightGrid]):
    step0 = steps_line[0]
    step0.print(True)
    print()
    
    step1 = lg.step(steps_line[0])
    step1.print(True)
    print()

