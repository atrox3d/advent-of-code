    
import itertools
import string
from typing import Generator
from dataclasses import dataclass, field


from shop import Shop, ShopItem, Weapon, Armor, Ring 

@dataclass
class Build:
    weapon:Weapon
    armor:Armor
    lring:Ring
    rring:Ring
    total_damage:int = 0
    total_armor:int = 0
    total_cost:int = 0

    def __post_init__(self):
        self.total_damage = sum(item.damage for item in self.items())
        self.total_armor = sum(item.armor for item in self.items())
        self.total_cost =  sum(item.cost for item in self.items())

    def items(self) -> tuple[Weapon, Armor, Ring, Ring]:
        return self.weapon, self.armor, self.lring, self.rring
    
    def get_stats(self) -> tuple[int, int, int]:
        return self.total_damage, self.total_armor, self.total_cost


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

    for build in get_builds(shop):
        print(build.weapon.name, build.armor.name, build.lring.name, build.rring.name,
               build.get_stats())

