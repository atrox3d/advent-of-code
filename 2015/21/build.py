from dataclasses import dataclass

try:
    from shop import Shop, ShopItem, Weapon, Armor, Ring
except:
    from .shop import Shop, ShopItem, Weapon, Armor, Ring

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
