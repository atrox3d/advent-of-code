from pathlib import Path
import pytest
import json
import itertools

try:
    from happiness import get_happiness, totals, rpermute, get_combo_value
except:
    from .happiness import get_happiness, totals, rpermute, get_combo_value

@pytest.fixture
def quiz_input():
    test_path = Path(__file__).parent / 'test_data.txt'
    with open(test_path, 'r') as fp:
        return [line.rstrip() for line in  fp.readlines()]

@pytest.fixture
def happiness(quiz_input) -> dict[str:dict[str:int]]:
    return get_happiness(quiz_input)

def test_happiness(happiness):
    # happiness = get_happiness(quiz_input)
    # print(json.dumps(happiness, indent=2))

    combo = get_combo_value(happiness, 'Alice', 'David')
    assert combo['total'] == 44

    combo = get_combo_value(happiness, 'Alice', 'Bob')
    assert combo['total'] == 137

    combo = get_combo_value(happiness, 'Carol', 'Bob')
    assert combo['total'] == 53

    combo = get_combo_value(happiness, 'Carol', 'David')
    assert combo['total'] == 96

def test_rpermute(happiness):
    names = [name for name in happiness]
    rpermutations = rpermute(names, as_list=True, use_recursive=True)
    permutations = [list(combo) for combo in itertools.permutations(names)]
    assert len(permutations) == len(rpermutations)
    assert rpermutations == permutations

def test_totals(happiness):
    names = [name for name in happiness]
    combos = rpermute(names)
    tot = totals(happiness, combos)
    assert max(tot) == 330
