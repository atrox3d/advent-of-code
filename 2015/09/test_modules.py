import re
import pytest
from pathlib import Path
import io

try:
    import parsing
except:
    from . import parsing

REGEX = r'^(\w+) to (\w+) = (\d+)$'
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

def test_parse_distances(test_input, parsed):
    assert parsed == parsing.parse_distances(test_input)
