from pathlib import Path

from shop_item import (
    ShopItem,
    Weapon,
    Ring,
    Armor,
)

class Shop:

    def __init__(self, filename:str, path:Path=Path(__file__).parent) -> list[str]:
        self.filename = filename
        self.path = path
        # self._data = None
        # self._items_dict = None
        self._items = None
        self.load()

    @staticmethod
    def _load(filename:str, path:Path=Path(__file__).parent) -> list[str]:
        with open(str(path / filename )) as fp:
            data = fp.read().splitlines()
        return data

    @staticmethod
    def _parse(data:list[str]) -> dict:
        items = {}
        klass = ShopItem
        for line in data:
            if ':' in line:
                category, *rest = line.split(':')
                items[category] = []
                match category:
                    case 'Weapons':
                        klass = Weapon
                    case 'Armors':
                        klass = Armor
                    case 'Rings':
                        klass = Ring
                    case _:
                        raise ValueError(f'unknown {category=}')
            else:
                match line.split():
                    case name, cost, damage, armor:
                        item = klass(category, name, int(cost), int(damage), int(armor))
                        items[category].append(item)
                    case name, modifier, cost, damage, armor:
                        item = klass(category, f'{name} {modifier}', int(cost), int(damage), int(armor))
                        items[category].append(item)
                    case '':
                        pass
        return items

    def load(self) -> list[ShopItem]:
        data = self._load(self.filename, self.path)
        items_dict = self._parse(data)
        self._items = [item for category, items in items_dict.items() for item in items]

    def items(self):
        return [item for item in self._items]

    @staticmethod
    def _sortby(data:list[ShopItem], category:bool=None, name:bool=None, cost:bool=None, 
                damage:bool=None, armor:bool=None, qty:bool=None, reverse=False
        ) -> list[ShopItem]:
        keys = {k:v for k, v in locals().items() if v is True and k not in 'data reverse'.split()}
        # print(f'{keys=}', end='\n\n')
        return sorted(data[:], key=lambda x:[getattr(x, k) for k in keys], reverse=reverse)
    
    def _get_category(self, klass) -> list[ShopItem]:
        if not issubclass(klass, ShopItem):
            raise TypeError(f'unknown class {klass.__name__}')
        return [item for item in self._items if isinstance(item, klass)]

    def weapons(self):
        return self._get_category(Weapon)

    def armors(self):
        return self._get_category(Armor)

    def rings(self):
        return self._get_category(Ring)

if __name__ == '__main__':
    shop = Shop('shop.txt')
    print(shop.items(), end='\n\n')
    print(shop.weapons(), end='\n\n')
    print(shop.armors(), end='\n\n')
    print(shop.rings(), end='\n\n\n\n')

    [print(item) for item in 
     shop._sortby(shop.items(), category=True, cost=True, reverse=False)]
