import json
from pathlib import Path
import pytest

try:
    import ingredient as ing
except:
    from . import ingredient as ing

@pytest.fixture
def quiz_input() -> str:
    test_file = Path(__file__).parent / 'test.txt'
    with open(test_file, 'r') as fp:
        return fp.read()

@pytest.fixture
def ingredients(quiz_input) -> dict:
    return ing.parse_ingredients(quiz_input)

def test_parse(quiz_input):
    ingredients = ing.parse_ingredients(quiz_input)
    # print(json.dumps(ingredients, indent=2))
    assert isinstance(ingredients, dict)

    assert len(ingredients) == 2

    for name, stats in ingredients.items():
        assert isinstance(stats, dict)

        for name, value in stats.items():
            assert isinstance(value, int)

        assert 'capacity' in stats
        assert 'durability' in stats
        assert 'flavor' in stats
        assert 'texture' in stats
        assert 'calories' in stats

def test_get_property_names(ingredients):
    assert ing.get_property_names(ingredients) == ['capacity', 'durability', 'flavor', 'texture', 'calories']

def test_get_mixes():
    assert list(ing.get_mixes(spoons=10, ingredients=2)) == [
            (1, 9), (2, 8), (3, 7), 
            (4, 6), (5, 5), (6, 4), 
            (7, 3), (8, 2), (9, 1)
        ]

def test_get_mixes_product():
    assert list(ing.get_mixes_product(spoons=10, ingredients=2)) == [
            (1, 9), (2, 8), (3, 7), 
            (4, 6), (5, 5), (6, 4), 
            (7, 3), (8, 2), (9, 1)
        ]

def test_get_property_score(ingredients):
    mix = (44, 56)
    assert ing.get_property_score( 'capacity', mix, ingredients ) == 68
    assert ing.get_property_score( 'durability', mix, ingredients ) == 80
    assert ing.get_property_score( 'flavor', mix, ingredients ) == 152
    assert ing.get_property_score( 'texture', mix, ingredients ) == 76

def test_get_scores(ingredients):
    mix = (44, 56)
    assert list(ing.get_scores([mix], ingredients, 'calories')) == [62842880]

def test_get_max_score(ingredients):
    mixes = ing.get_mixes(100, 2)
    assert ing.get_max_score(mixes, ingredients, 'calories') == 62842880

def test_find_calories(ingredients):
    mixes = ing.get_mixes(100, 2)
    result = list(ing.find_calories(mixes, ingredients, 500))
    print(result)
    [(score, calories)] = result
    assert score == 57600000
    assert calories == 500
