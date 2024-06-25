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
