from pathlib import Path

from shop_item import (
    ShopItem,
    Weapon,
    Ring,
    Armor,
)

class Shop:

    def __init__(self, filename:str='shop.txt', path:Path=Path(__file__).parent) -> list[str]:
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

    def items(self, sortby:str=None, reverse=False):
        return self._sortby([item for item in self._items], sortby, reverse)

    @staticmethod
    def _sortby(data:list[ShopItem], fields:str=None, reverse=False
        ) -> list[ShopItem]:
        if fields is None:
            return data
        keys = fields.split()
        print(f'{keys=}', end='\n\n')
        return sorted(data[:], key=lambda x:[getattr(x, k) for k in keys], reverse=reverse)
    
    def _get_category(self, klass) -> list[ShopItem]:
        if not issubclass(klass, ShopItem):
            raise TypeError(f'unknown class {klass.__name__}')
        return [item for item in self._items if isinstance(item, klass)]

    def weapons(self, sortby:str=None, reverse=False):
        return self._sortby(self._get_category(Weapon), sortby, reverse)

    def armors(self, sortby:str=None, reverse=False):
        return self._sortby(self._get_category(Armor), sortby, reverse)

    def rings(self, sortby:str=None, reverse=False):
        return self._sortby(self._get_category(Ring), sortby, reverse)

if __name__ == '__main__':
    shop = Shop()
    [print(item) for item in shop.weapons(sortby='cost damage')]
    [print(item) for item in shop.armors(sortby='cost armor')]
    [print(item) for item in shop.rings(sortby='name armor damage')]
    [print(item) for item in shop.items(sortby='name armor damage')]
    # [print(item) for item in 
    #  shop._sortby(shop.items(), None, reverse=True)]
