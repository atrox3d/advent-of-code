from y2015.d22.basegame.build import Build
from y2015.d22.basegame.character import Character


class Boss(Character):
    def equip(self, build:Build) -> None:
        raise AttributeError('Boss cannot equip')
