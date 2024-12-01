import pytest

# from y2015.d22.game.character import Character
from y2015.d22.game.boss import Boss
from y2015.d22.game.character import Character
from y2015.d22.game.spell import MagicMissile, Poison
from y2015.d22.game.wizard import Wizard

@pytest.fixture
def boss():
    boss = Boss(
        'Boss',
        13,
        8,
        0
    )
    assert boss.hitpoints == 13
    assert boss.damage == 8
    return boss

@pytest.fixture
def player():
    player = Wizard(
        'Player',
        10,
        0,
        0,
        250
    )
    assert player.hitpoints == 10
    assert player.mana == 250
    return player

def test_fixtures(player, boss):
    pass

def test_example(player, boss):
    def turn(player:Character, boss:Character):
        player.turn()
        boss.turn()
    '''
    --                   Player turn --
    - Player has 10 hit points, 0 armor, 250 mana
    - Boss has 13 hit points
    '''
    turn(player, boss)
    assert player.hitpoints == 10
    assert player.armor == 0
    assert player.mana == 250
    assert boss.hitpoints == 13
    '''
    + Player casts Poison.
    '''
    poison = player.cast(Poison, boss)
    assert poison.timer == 6

    '''
    --                   Boss turn --
    - Player has 10 hit points, 0 armor, 77 mana
    - Boss has 13 hit points
    
    ******* -> Poison deals 3 damage; its timer is now 5.
    '''
    assert boss.hitpoints == 13
    turn(player, boss)
    assert boss.hitpoints == 10
    assert player.hitpoints == 10
    assert player.armor == 0
    assert player.mana == 77
    assert poison.timer == 5
    '''
        + Boss attacks for 8 damage.
    '''
    boss.attack(player)


    '''
    --                     Player turn --
        - Player has 2 hit points, 0 armor, 77 mana
        - Boss has 10 hit points
    '''
    assert boss.hitpoints == 10
    turn(player, boss)
    assert boss.hitpoints == 7
    assert player.hitpoints == 2
    assert player.armor == 0
    assert player.mana == 77
    assert poison.timer == 4

    '''
        ********Poison deals 3 damage; its timer is now 4.
        + Player casts Magic Missile, dealing 4 damage.
    '''
    player.cast(MagicMissile, boss)


    '''
    --                      Boss turn --
    - Player has 2 hit points, 0 armor, 24 mana
    - Boss has 3 hit points
    '''
    assert boss.hitpoints == 3
    turn(player, boss)
    assert boss.hitpoints == 0
    assert player.hitpoints == 2
    assert player.armor == 0
    assert player.mana == 24
    '''
    *** Poison deals 3 damage. This kills the boss, and the player wins.
    '''
    

