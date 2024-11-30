from pathlib import Path

import pytest

from y2015.d22.basegame import boss, build, shop_item

def test_boss_from_file():
    char = boss.Boss.from_file('Sauron')
    print(char)
    assert char.name == 'Sauron'
    assert char.hitpoints == 104
    assert char.damage == 8
    assert char.armor == 1
    
def test_char_build():
    char = boss.Boss.from_file('Sauron')
    print(char)

    b = build.Build(
        shop_item.Weapon('Weapons', 'sword', 10, 10, 0, 1),
        shop_item.Weapon('Armors', 'armor', 10, 0, 10, 1),
        shop_item.Weapon('Rings', 'left ring', 10, 1, 0, 1),
        shop_item.Weapon('Rings', 'right ring', 10, 0, 1, 1)
    )

    with pytest.raises(AttributeError):
        char.equip(b)
