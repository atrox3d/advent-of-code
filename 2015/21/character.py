from dataclasses import dataclass
from pathlib import Path

from build import Build

@dataclass
class Character:
    name: str
    hitpoints: int
    damage: int
    armor: int

    @classmethod
    def from_file(cls, name, filename:str='input1.txt', path:Path=Path(__file__).parent) -> 'Character':
        with open(path / filename) as fp:
            lines = fp.read()

        char = cls(name, 0, 0, 0)
        for line in lines.splitlines():
            match line.split():
                case 'Hit', 'Points:', hitpoints:
                    char.hitpoints = int(hitpoints)
                case 'Damage:', damage:
                    char.damage = int(damage)
                case 'Armor:', armor:
                    char.armor = int(armor)
        
        return char
    
    def equip(self, build:Build) -> None:
        self.damage = build.total_damage
        self.armor = build.total_armor

    def attack(self, opponent:'Character') -> int:
        '''
        In this game, the player (you) and the enemy (the boss) take turns attacking. 
        The player always goes first. Each attack reduces the opponent's hit points 
        by at least 1. The first character at or below 0 hit points loses.

        Damage dealt by an attacker each turn is equal to the attacker's damage score 
        minus the defender's armor score. 
        An attacker always does at least 1 damage. 
        So, if the attacker has a damage score of 8, and the defender has an armor score of 3, 
        the defender loses 5 hit points. 
        If the defender had an armor score of 300, the defender would still lose 1 hit point.
        '''
        damage = self.damage - opponent.armor
        damage = damage if damage > 0 else 1
        opponent.hitpoints -= damage
        return opponent.hitpoints

if __name__ == '__main__':
    char = Character.from_file('boss')
    print(char)
