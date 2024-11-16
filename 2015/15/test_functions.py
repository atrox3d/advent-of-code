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
