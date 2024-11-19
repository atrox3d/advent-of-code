import pytest
import re
try:
    import gifts
except:
    from . import gifts

@pytest.fixture
def test_text() -> str:
    return '''House 1 got 10 presents.
House 2 got 30 presents.
House 3 got 40 presents.
House 4 got 70 presents.
House 5 got 60 presents.
House 6 got 120 presents.
House 7 got 80 presents.
House 8 got 150 presents.
House 9 got 130 presents.
'''

def test_values(test_text:str):
    values = []
    for line in test_text.splitlines():
        # values = re.match(r'^House (\d) ', line)
        # print(values)
        match line.split():
            case 'House', house, 'got', presents, 'presents.':
                values.append((int(house), int(presents)))
    print(values)
    return values

@pytest.mark.parametrize(
    'house, presents', [
            (1, 10), 
            (2, 30), 
            (3, 40), 
            (4, 70), 
            (5, 60), 
            (6, 120), 
            (7, 80), 
            (8, 150), 
            (9, 130)
        ]
)
def test_get_house(house, presents):
    assert presents == gifts.get_presents_per_house(house)


