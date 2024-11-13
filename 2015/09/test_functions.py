import json
import pytest
from pathlib import Path
import io

try:
    import functions
except:
    from . import functions

TEST_INPUT = '''London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
'''

@pytest.fixture
def test_input() -> str:
    with io.StringIO(TEST_INPUT) as fp:
        return fp.read()

@pytest.fixture
def parsed() -> list[tuple[str, str, int]]:
    return [
            ('London', 'Dublin', 464), 
            ('London', 'Belfast', 518), 
            ('Dublin', 'Belfast', 141)
        ]

@pytest.fixture
def maap() -> dict:
    return {
        "London": {
            "Dublin": 464,
            "Belfast": 518
        },
        "Dublin": {
            "London": 464,
            "Belfast": 141
        },
        "Belfast": {
            "London": 518,
            "Dublin": 141
        }
    }

@pytest.fixture
def cities():
    return {'Belfast', 'London', 'Dublin'}

@pytest.fixture
def permutations():
    return [
        ['Dublin', 'London', 'Belfast'], 
        ['Dublin', 'Belfast', 'London'], 
        ['London', 'Dublin', 'Belfast'], 
        ['London', 'Belfast', 'Dublin'], 
        ['Belfast', 'Dublin', 'London'], 
        ['Belfast', 'London', 'Dublin']
    ]

@pytest.fixture
def routes():
    return {
        ('Dublin', 'London', 'Belfast'): 982, 
        ('Dublin', 'Belfast', 'London'): 659, 
        ('London', 'Dublin', 'Belfast'): 605, 
        ('London', 'Belfast', 'Dublin'): 659, 
        ('Belfast', 'Dublin', 'London'): 605, 
        ('Belfast', 'London', 'Dublin'): 982
    }

def test_parse_distances(test_input, parsed):
    assert parsed == functions.parse_distances(test_input)

def test_build_map(parsed, maap):
    assert maap == functions.build_map(parsed)

def test_get_city_list(parsed, cities):
    assert cities == functions.get_city_list(parsed)

def test_rpermute(cities, permutations):
    assert sorted(permutations) == sorted(functions.rpermute(cities))

def test_get_routes(routes, permutations, maap):
    assert sorted(routes) == sorted(functions.get_routes(permutations, maap))

def test_shortest_distance(routes):
    assert min(routes.values()) == 605

def test_longest_distance(routes):
    assert max(routes.values()) == 982

def test_example1(test_input):
    distances = functions.parse_distances(test_input)
    maap = functions.build_map(distances)
    cities = functions.get_city_list(distances)
    permutations = functions.rpermute(cities)
    routes = functions.get_routes(permutations, maap)
    result = min(routes.values())
    assert result == 605

def test_example2(test_input):
    distances = functions.parse_distances(test_input)
    maap = functions.build_map(distances)
    cities = functions.get_city_list(distances)
    permutations = functions.rpermute(cities)
    routes = functions.get_routes(permutations, maap)
    result = max(routes.values())
    assert result == 982


