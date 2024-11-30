from pathlib import Path

from y2015.d22.game import character
from y2015.d22.basegame import build, shop_item

def test_char_build():
    char = character.Character(
        'Conan',
        104,
        8,
        1
    )
    print(char)

    assert char.name == 'Conan'
    assert char.hitpoints == 104
    assert char.damage == 8
    assert char.armor == 1

    b = build.Build(
        shop_item.Weapon('Weapons', 'sword', 10, 10, 0, 1),
        shop_item.Weapon('Armors', 'armor', 10, 0, 10, 1),
        shop_item.Weapon('Rings', 'left ring', 10, 1, 0, 1),
        shop_item.Weapon('Rings', 'right ring', 10, 0, 1, 1)
    )
    char.equip(b)
    print(char)
    assert char.damage == b.total_damage
    assert char.armor == b.total_armor
    