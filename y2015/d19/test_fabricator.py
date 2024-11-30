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
    test_file = Path(__file__).parent / 'test2.txt'
    return test_file

@pytest.fixture
def quiz_input(test_file) -> str:
    with open(test_file, 'r') as fp:
        return fp.read()

@pytest.fixture
def replacements(quiz_input):
    return parse_rules(quiz_input)

def test_build_steps(replacements):
    santa = 'HOHOHO'
    target = 'HOH'
    count,steps = build_steps(target, replacements)
    assert count == 3

    count, steps = build_steps(santa, replacements)
    print(count, steps)
    assert count == 6

