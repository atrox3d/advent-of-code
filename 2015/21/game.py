    
import itertools
import string
from typing import Generator
from dataclasses import dataclass, field

from shop import Shop
from character import Character
from build import Build

def get_builds(shop:Shop) -> Generator[Build, None, None]:
    weapons = shop.weapons()
    armors = shop.armors()
    leftrings = shop.rings()
    rightrings = shop.rings()
    assert leftrings is not rightrings, 'fuck'
    assert leftrings == rightrings, 'fuck'

    for weapon, armor, lring, rring in itertools.product(weapons, armors, leftrings, rightrings):
        if lring is not rring:
            build = Build(weapon, armor, lring, rring)
            yield build
    

if __name__ == '__main__':
    shop = Shop()
    boss = Character.from_file()
    player = Character(100, 0, 0)
    
    print(f'{boss = }')
    print(f'{player = }')

    for build in get_builds(shop):
        # print(build.weapon.name, build.armor.name, build.lring.name, build.rring.name,
            #    build.get_stats())
        player.equip(build)
        print(f'{player = }')
