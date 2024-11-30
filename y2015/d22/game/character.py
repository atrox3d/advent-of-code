from dataclasses import dataclass, field

from y2015.d22.basegame.character import Character as BaseChar
# from y2015.d22.game.spell import Spell

@dataclass
class Character(BaseChar):
    mana:int = 0
    spells:list['Spell'] = field(default_factory=list)

    def turn(self):
        self.apply_effects()
    
    def apply_effects(self):
        for spell in self.spells:
            if spell.timer > 0:
                spell.effect()
                spell.timer -= 1
        
        for spell in self.spells:
            if spell.timer == 0:
                spell.remove()
                self.spells.remove(spell)
    
    def attack(self, opponent: 'Character') -> int:
        # self.apply_effects()
        # opponent.apply_effects()
        return super().attack(opponent)