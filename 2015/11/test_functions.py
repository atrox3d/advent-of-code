import pytest

try:
    from increment import increment
    from rincrement import rincrement
    from valid import is_valid, valid_chars, forbidden
    from doubles import has_doubles
    from straight import has_straight, get_straights
except:
    from .increment import increment
    from .rincrement import rincrement
    from .valid import is_valid, valid_chars, forbidden
    from .doubles import has_doubles
    from .straight import has_straight, get_straights

def test_get_straights():
    assert 'abc' in get_straights(3)
    assert 'efg' in get_straights(3)
    assert 'abcxyz' not in get_straights(3)
    assert 'abczzz' not in get_straights(3)

def test_has_straight():
    assert has_straight('abcaaa')
    assert has_straight('aaaaabcaaaaa')
    assert has_straight('xyz123')
