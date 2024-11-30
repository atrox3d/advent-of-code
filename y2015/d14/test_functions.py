import pytest
from pathlib import Path
import json

try:
    import functions
except:
    from . import functions

@pytest.fixture
def quiz_input():
    test_file = Path(__file__).parent / 'test.txt'
    with open(test_file, 'r') as fp:
        return fp.readlines()

@pytest.fixture
def reindeers():
    return {
        "Comet": {
            "speed": 14,
            "flytime": 10,
            "resttime": 127
        },
        "Dancer": {
            "speed": 16,
            "flytime": 11,
            "resttime": 162
        }
    }

def test_parse(quiz_input, reindeers):
    print(quiz_input)
    data = functions.parse_reindeers(quiz_input)
    assert data == reindeers

def test_race1(reindeers):
    second01 = functions.race1(1, reindeers)
    assert [('Dancer', 16)] == second01

    second10 = functions.race1(10, reindeers)
    assert [('Dancer', 160)] == second10

    second11 = functions.race1(11, reindeers)
    assert [('Dancer', 176)] == second11

    second12 = functions.race1(12, reindeers)
    assert [('Dancer', 176)] == second12

    second138 = functions.race1(138, reindeers)
    assert [('Dancer', 176)] == second138

    second1000 = functions.race1(1000, reindeers)
    assert [('Comet', 1120)] == second1000

def test_race2(reindeers):
    second01 = functions.race2(1, reindeers)
    assert ('Dancer', 1) == second01

    second140 = functions.race2(140, reindeers)
    assert ('Dancer', 139) == second140

    second1000 = functions.race2(1000, reindeers)
    assert ('Dancer', 689) == second1000









