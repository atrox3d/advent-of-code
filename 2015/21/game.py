    
import itertools
import string
from typing import Generator
from dataclasses import dataclass, field

from shop import Shop
from character import Character
from build import Build

def get_builds(shop:Shop) -> Generator[Build, None, None]:
    weapons = shop.weapons()
    armors = shop.armors()
    leftrings = shop.rings()
    rightrings = shop.rings()
    assert leftrings is not rightrings, 'fuck'
    assert leftrings == rightrings, 'fuck'

    for weapon, armor, lring, rring in itertools.product(weapons, armors, leftrings, rightrings):
        if lring is not rring:
            build = Build(weapon, armor, lring, rring)
            yield build
def fight(player:Character, boss:Character) -> Character:
    turn = 0
    while player.hitpoints > 0 and boss.hitpoints > 0:
        if turn % 2 == 0:
            player.attack(boss)
        else:
            boss.attack(player)
        # print(f'player {player.hitpoints} - boss {boss.hitpoints}')
        turn += 1
    
    if player.hitpoints > 0:
        winner = player
    elif boss.hitpoints > 0:
        winner = boss
    else:
        raise ValueError('at least one character must be alive')
    return winner
        

if __name__ == '__main__':
    shop = Shop()
    
    # print(f'{boss = }')
    # print(f'{player = }')


    winning_builds_costs = []
    for build in get_builds(shop):
        # print(build.weapon.name, build.armor.name, build.lring.name, build.rring.name,
            #    build.get_stats())
        boss = Character.from_file('boss')
        player = Character('player', 100, 0, 0)
        player.equip(build)
        winner = fight(player, boss)
        if winner is player:
            print(f'{winner = }\n{build.total_cost = }')
            winning_builds_costs.append(build.total_cost)
    lower = min(winning_builds_costs)
    print(f'{lower = }')
    # return lower
    