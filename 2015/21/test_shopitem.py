try:
    import shop_item
except:
    from . import shop_item


def test_no_weapon():
    noweapon = shop_item.no_weapon
    assert noweapon.category == 'Weapons'
    assert noweapon.name == 'NoWeapon'
    assert noweapon.cost ==  0
    assert noweapon.damage ==  0
    assert noweapon.armor ==  0
    assert noweapon.qty == 1

def test_no_armor():
    noarmor = shop_item.no_armor
    assert noarmor.category == 'Armors'
    assert noarmor.name == 'NoArmor'
    assert noarmor.cost ==  0
    assert noarmor.damage ==  0
    assert noarmor.armor ==  0
    assert noarmor.qty == 1

def test_no_ring():
    noring = shop_item.no_ring
    assert noring.category == 'Rings'
    assert noring.name == 'NoRing'
    assert noring.cost ==  0
    assert noring.damage ==  0
    assert noring.armor ==  0
    assert noring.qty == 1

def test_shopitem():
    item = shop_item.ShopItem(
        'tests',
        'test',
        10,
        20,
        30,
        1
    )
    assert item.category == 'tests'
    assert item.name == 'test'
    assert item.cost == 10
    assert item.damage == 20
    assert item.armor == 30
    assert item.qty == 1
