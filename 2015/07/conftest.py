import pytest

@pytest.fixture
def circuit():
    return \
'''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
'''.splitlines()

@pytest.fixture
def gate_ports():
    return [
        ('123', 'x'),
        ('456', 'y'),
        ('x AND y', 'd'),
        ('x OR y', 'e'),
        ('x LSHIFT 2', 'f'),
        ('y RSHIFT 2', 'g'),
        ('NOT x', 'h'),
        ('NOT y', 'i'),
    ]

@pytest.fixture
def gates():
    return [
        [123, None, None],
        [456, None, None],
        ['x', 'AND', 'y'],
        ['x', 'OR', 'y'],
        ['x', 'LSHIFT', 2],
        ['y', 'RSHIFT', 2],
        ['NOT', None, 'x'],
        ['NOT', None, 'y'],
    ]

@pytest.fixture
def signals():
    return {
        'd': 72,
        'e': 507,
        'f': 492,
        'g': 114,
        'h': 65412,
        'i': 65079,
        'x': 123,
        'y': 456,
    }
