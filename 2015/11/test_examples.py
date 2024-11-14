try:
    from increment import increment
    from rincrement import rincrement
    from valid import is_valid, valid_chars, forbidden
    from doubles import has_doubles
    from straight import has_straight
except:
    from .increment import increment
    from .rincrement import rincrement
    from .valid import is_valid, valid_chars, forbidden
    from .doubles import has_doubles
    from .straight import has_straight

def test_example1():
    '''
    hijklmmn meets the first requirement (because it contains the straight hij) 
    but fails the second requirement requirement (because it contains i and l).
    '''
    assert has_straight('hijklmmn', valid_chars) is False

def test_example2():
    '''
    abbceffg meets the third requirement (because it repeats bb and ff) 
    but fails the first requirement.    
    '''
    assert has_doubles('abbceffg') is True

def test_example3():
    '''
    abbcegjk fails the third requirement, because it only has one double
    letter (bb)
    '''
    assert has_doubles('abbcegjk') is False

def test_example4():
    '''
    The next password after abcdefgh is abcdffaa
    '''
    result = increment('abcdefgh')
    while not is_valid(result):
        result = increment(result)
    assert result == 'abcdffaa'

def test_example5():
    '''
    The next password after ghijklmn is ghjaabcc, because you eventually 
    skip all the passwords that start with ghi..., since i is not allowed
    '''
    result = increment('ghijklmn')
    while not is_valid(result):
        result = increment(result)
    assert result == 'ghjaabba'
