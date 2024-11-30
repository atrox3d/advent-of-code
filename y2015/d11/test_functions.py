import pytest

try:
    from increment import increment
    from rincrement import rincrement
    from valid import is_valid, valid_chars, forbidden, check_chars
    from doubles import has_doubles
    from straight import has_straight, get_straights
except:
    from .increment import increment
    from .rincrement import rincrement
    from .valid import is_valid, valid_chars, forbidden, check_chars
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

def test_doubles():
    assert has_doubles('aa12345bb')
    assert has_doubles('aabb')
    assert not has_doubles('aabbaa')
    assert has_doubles('aabbccc')
    assert not has_doubles('aabbcccc')
    assert not has_doubles('abcdefgh')
    assert has_doubles('ghjaaabb')
    assert has_doubles('gjaaabcc')
    assert has_doubles('abcdffaa')
    assert has_doubles('ghjaabcc')
    assert has_doubles('gjaabbcd')

def test_check_chars():
    assert check_chars(valid_chars, valid_chars, forbidden)
    assert not check_chars(forbidden, valid_chars, forbidden)

def test_increment():
    assert increment('a') == 'b'
    assert increment('ab') == 'ac'
    assert increment('az') == 'ba'
