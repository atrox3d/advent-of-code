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
        self._data = None
        self._items_dict = None
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
        self._data = self._load(self.filename, self.path)
        self._items_dict = self._parse(self._data)
        self._items = [item for category, items in self._items_dict.items() for item in items]

    def items(self):
        return [item for item in self._items]

if __name__ == '__main__':
    shop = Shop('shop.txt')
    print(shop.items())

