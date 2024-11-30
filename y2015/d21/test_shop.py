from pathlib import Path


try:
    import shop
except:
    from . import shop


def test_shop_from_file():
    filepath = Path(__file__).parent / 'shop.txt'
    assert filepath.exists()

    s = shop.Shop()
    assert s.filename == 'shop.txt'
    assert s.filename == 'shop.txt'
    assert s.path == filepath.parent

    s = shop.Shop(filepath.name, filepath.parent)
    assert s.filename == 'shop.txt'
    assert s.path == filepath.parent

def test_items():
    s = shop.Shop()
    assert len(s.items()) == 18


def test_categories():
    s = shop.Shop()
    categories = s.categories()
    print(categories)
    assert categories == ['Armors', 'Rings', 'Weapons']

def test_weapons():
    s = shop.Shop()
    for weapon in s.weapons():
        assert weapon.category == 'Weapons'

def test_armors():
    s = shop.Shop()
    for weapon in s.armors():
        assert weapon.category == 'Armors'

def test_rings():
    s = shop.Shop()
    for weapon in s.rings():
        assert weapon.category == 'Rings'
