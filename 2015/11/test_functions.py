from xml.dom import HierarchyRequestErr


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

def test_has_straight():
    print(has_straight('yza'))