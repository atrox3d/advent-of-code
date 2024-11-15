from pathlib import Path
import pytest
import json

try:
    from happiness import get_happiness, totals, rpermute, get_combo_value
except:
    from .happiness import get_happiness, totals, rpermute, get_combo_value

@pytest.fixture
def quiz_input():
    test_path = Path(__file__).parent / 'test_data.txt'
    with open(test_path, 'r') as fp:
        return [line.rstrip() for line in  fp.readlines()]

def test_happiness(quiz_input):
    happiness = get_happiness(quiz_input)
    print(json.dumps(happiness, indent=2))

    combo = get_combo_value(happiness, 'Alice', 'David')
    assert combo['total'] == 44

    combo = get_combo_value(happiness, 'Alice', 'Bob')
    assert combo['total'] == 137

    combo = get_combo_value(happiness, 'Carol', 'Bob')
    assert combo['total'] == 53

    combo = get_combo_value(happiness, 'Carol', 'David')
    assert combo['total'] == 96


