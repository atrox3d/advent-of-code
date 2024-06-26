from dataclasses import dataclass

@dataclass
class ShopItem:
    category: str
    name: str
    cost: int
    damage: int
    armor: int
    qty: int = 1

class Weapon(ShopItem): pass
class Armor(ShopItem): pass
class Ring(ShopItem): pass

no_weapon =Weapon('Weapons', 'NoWeapon', 0, 0, 0)
no_armor = Armor('Armors', 'NoArmor', 0, 0, 0)
no_ring = Ring('Rings', 'NoRing', 0, 0, 0)
