from dataclasses import dataclass
from pathlib import Path

@dataclass
class Character:
    hitpoints:int
    damage:int
    armor:int

    @classmethod
    def from_file(cls, filename:str='input1.txt', path:Path=Path(__file__).parent) -> 'Character':
        with open(path / filename) as fp:
            lines = fp.read()

        char = cls(0, 0, 0)
        for line in lines.splitlines():
            match line.split():
                case 'Hit', 'Points:', hitpoints:
                    char.hitpoints = hitpoints
                case 'Damage:', damage:
                    char.damage = damage
                case 'Armor:', armor:
                    char.armor = armor
        
        return char


if __name__ == '__main__':
    char = Character.from_file()
    print(char)
