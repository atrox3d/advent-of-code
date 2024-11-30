from y2015.d22.game.character import Character


class Spell:
    def __init__(
            self, 
            caster:Character, 
            target:Character,
            name:str=None,
            cost:int=0,
            timer:int=None
    ) -> None:
        self.caster = caster
        self.target = target
        self.name = name
        self.cost = cost
        self.timer = timer
    
    def effect(self):
        raise NotImplementedError
    
    def remove(self):
        pass

class Poison(Spell):
    '''
    '''
    def __init__(self, caster: Character, target: Character) -> None:
        super().__init__(
            caster, target, 
            cost=173, 
            name='Poison',
            timer=6
        )
    
    def effect(self):
        self.target.hitpoints -= 3

class MagicMissile(Spell):
    '''
    '''
    def __init__(self, caster: Character, target: Character) -> None:
        super().__init__(
            caster, target, 
            cost=53, 
            name='Magic Missile',
            timer=None
        )
    
    def effect(self):
        self.target.hitpoints -= 4
    

class Recharge(Spell):
    '''
    Recharge costs 229 mana. 
    It starts an effect that lasts for 5 turns. 
    At the start of each turn while it is active, 
    it gives you 101 new mana.
    '''
    def __init__(self, caster: Character, target: Character) -> None:
        super().__init__(
            caster, target, 
            cost=229, 
            name='Recharge',
            timer=5
        )
    
    def effect(self):
        self.target.mana += 101

class Shield(Spell):
    '''
    Shield costs 113 mana. 
    It starts an effect that lasts for 6 turns. 
    While it is active, your armor is increased by 7.
    '''
    def __init__(self, caster: Character, target: Character) -> None:
        super().__init__(
            caster, target, 
            cost=113, 
            name='Shield',
            timer=6
        )
    
    def effect(self):
        if self.timer == 6:
            self.target.armor += 7
    
    def remove(self):
        self.target.armor -= 7


class Drain(Spell):
    '''
    Drain costs 73 mana. 
    It instantly does 2 damage 
    and heals you for 2 hit points.

    '''
    def __init__(self, caster: Character, target: Character) -> None:
        super().__init__(
            caster, target, 
            cost=73, 
            name='Drain',
            timer=None
        )
    
    def effect(self):
        self.target.hitpoints -= 2
        self.caster.hitpoints += 2
