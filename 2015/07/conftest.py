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
    return {
        'x': '123',
        'y': '456',
        'd': 'x AND y',
        'e': 'x OR y',
        'f': 'x LSHIFT 2',
        'g': 'y RSHIFT 2',
        'h': 'NOT x',
        'i': 'NOT y',
    }

@pytest.fixture
def gates():
    return {
        'x': [123, None, None],
        'y': [456, None, None],
        'd': ['x', 'AND', 'y'],
        'e': ['x', 'OR', 'y'],
        'f': ['x', 'LSHIFT', 2],
        'g': ['y', 'RSHIFT', 2],
        'h': ['NOT', None, 'x'],
        'i': ['NOT', None, 'y'],
    }

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

@pytest.fixture
def strwires():
    return {
        'x': 'x = 123',
        'y': 'y = 456',
        'd': 'd = x AND y',
        'e': 'e = x OR y',
        'f': 'f = x LSHIFT 2',
        'g': 'g = y RSHIFT 2',
        'h': 'h = NOT x',
        'i': 'i = NOT y',
    }
