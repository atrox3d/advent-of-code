from dataclasses import dataclass
from y2015.d22.basegame.character import Character as BaseChar
from y2015.d22.game.character import Character
from y2015.d22.game.spell import Spell

class InsufficientMana(Exception): pass

@dataclass
class Wizard(Character):

    def attack(self, opponent: Character) -> int:
        # return super().attack(opponent)
        raise AttributeError('Wizard cannot attack')
    
    def use_mana(self, spell:Spell):
        if self.mana < spell.cost:
            raise InsufficientMana
        self.mana -= spell.cost

    def cast(self, spell_class:Spell, target:Character) -> Spell:

        # self.apply_effects()
        # target.apply_effects()

        spell:Spell = spell_class(self, target)
        print(f'casting {spell.name} @ {spell.cost} mana')
        self.use_mana(spell)

        if spell.timer is None:
            spell.effect()
        else:
            target.spells.append(spell)
        
        return spell
