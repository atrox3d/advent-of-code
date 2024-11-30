try:
    import build, shop_item
except:
    from . import build, shop_item


def test_build():
    b = build.Build(
        shop_item.Weapon('Weapons', 'sword', 10, 10, 0, 1),
        shop_item.Weapon('Armors', 'armor', 10, 0, 10, 1),
        shop_item.Weapon('Rings', 'left ring', 10, 1, 0, 1),
        shop_item.Weapon('Rings', 'right ring', 10, 0, 1, 1)
    )
    assert (11, 11, 40) == b.get_stats()
    assert len(b.items()) == 4
