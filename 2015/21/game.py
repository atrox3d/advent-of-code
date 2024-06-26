    
import itertools
import string
from typing import Generator
from dataclasses import dataclass


from shop import Shop, ShopItem, Weapon, Armor, Ring 

@dataclass
class Build:
    weapon:Weapon
    armor:Armor
    lring:Ring
    rring:Ring

def get_builds(shop:Shop) -> Generator[Build, None, None]:
    weapons = shop.weapons()
    armors = shop.armors()
    leftrings = shop.rings()
    rightrings = shop.rings()
    assert leftrings is not rightrings, 'fuck'
    assert leftrings == rightrings, 'fuck'

    for weapon, armor, lring, rring in itertools.product(weapons, armors, leftrings, rightrings):
        if lring is not rring:
            # print(weapon.name, armor.name, lring.name, rring.name)
            # nametpl = (weapon.name, armor.name, lring.name, rring.name)
            build = Build(weapon, armor, lring, rring)
            yield build
    

if __name__ == '__main__':
    shop = Shop()

    for build in get_builds(shop):
        print(build.weapon.name, build.armor.name, build.lring.name, build.rring.name)
