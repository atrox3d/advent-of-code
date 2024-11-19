from pathlib import Path
import pytest

try:
    from calibrator import calibrate, indexall, multireplace
    from fabricator import build_steps
    from rules import parse_rules, parse_molecule
except:
    from .calibrator import calibrate, indexall, multireplace
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

@pytest.fixture
def replacements(quiz_input):
    return parse_rules(quiz_input)

def test_index_all():
    assert indexall('H', 'HOHOHOHOHOHO') == [0, 2, 4, 6, 8, 10]

def test_multi_replace():
    replaced = multireplace(
        'H',
        '_replace_',
        'HOHOHOHOHOHO'
    )
    assert replaced == [
            '_replace_OHOHOHOHOHO', 
            'HO_replace_OHOHOHOHO', 
            'HOHO_replace_OHOHOHO', 
            'HOHOHO_replace_OHOHO', 
            'HOHOHOHO_replace_OHO', 
            'HOHOHOHOHO_replace_O'
        ]

def test_calibrate(replacements):
    santas = 'HOHOHO'
    medicine = 'HOH'
    assert calibrate(santas, replacements) == {
            'HOHHHHO', 
            'HOHOOHO', 
            'HOHOHOO', 
            'OHOHOHO', 
            'HOOHOHO', 
            'HHHHOHO', 
            'HOHOHHH'
        }

    assert calibrate(medicine, replacements) == {
            'HHHH', 
            'HOHO', 
            'HOOH', 
            'OHOH'
        }
