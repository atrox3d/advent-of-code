from pathlib import Path
import pytest

try:
    from calibrator import calibrate
    from fabricator import build_steps
    from rules import parse_rules, parse_molecule
except:
    from .calibrator import calibrate
    from .fabricator import build_steps
    from .rules import parse_rules, parse_molecule


@pytest.fixture
def test_file():
    test_file = Path(__file__).parent / 'test1.txt'
    return test_file

@pytest.fixture
def quiz_input(test_file) -> str:
    with open(test_file, 'r') as fp:
        return fp.read()

def test_parse_rules(quiz_input):
    rules = parse_rules(quiz_input)
    assert rules == [
        {'H': 'HO'}, 
        {'H': 'OH'}, 
        {'O': 'HH'}
    ]

def test_parse_molecule(quiz_input):
    molecule = parse_molecule(quiz_input)
    assert molecule == 'molecule'
