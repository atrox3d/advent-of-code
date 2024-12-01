import pytest

# from y2015.d22.game.character import Character
from y2015.d22.game.boss import Boss
from y2015.d22.game.character import Character
from y2015.d22.game.spell import Drain, MagicMissile, Poison, Recharge, Shield
from y2015.d22.game.wizard import Wizard

@pytest.fixture
def boss():
    boss = Boss(
        'Boss',
        14,
        8,
        0
    )
    assert boss.hitpoints == 14
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
    -- Player turn --
    - Player has 10 hit points, 0 armor, 250 mana
    - Boss has 14 hit points
    '''
    turn(player, boss)
    assert player.hitpoints == 10
    assert player.armor == 0
    assert player.mana == 250
    assert boss.hitpoints == 14
    '''
    Player casts Recharge.
    '''
    recharge = player.cast(Recharge, player)

    '''
    -- Boss turn --
    - Player has 10 hit points, 0 armor, 21 mana
    - Boss has 14 hit points
    
    Recharge provides 101 mana; its timer is now 4.
    '''
    turn(player, boss)
    assert player.mana == 122
    assert recharge.timer == 4
    assert player.hitpoints == 10
    assert player.armor == 0
    assert boss.hitpoints == 14
    '''
        + Boss attacks for 8 damage.
    '''
    boss.attack(player)


    '''
    -- Player turn --
    - Player has 2 hit points, 0 armor, 122 mana
    - Boss has 14 hit points
    '''
    turn(player, boss)
    '''
    Recharge provides 101 mana; its timer is now 3.
    Player casts Shield, increasing armor by 7.
    '''
    assert recharge.timer == 3
    assert player.mana == 223

    assert player.hitpoints == 2
    assert player.armor == 0
    
    assert boss.hitpoints == 14
    player_mana = player.mana
    shield = player.cast(Shield, player)
    assert player.mana == player_mana - shield.cost

    assert player.mana == 110
    turn(player, boss)
    assert player.mana == 211

    '''
    -- Boss turn --
    - Player has 2 hit points, 7 armor, 110 mana
    - Boss has 14 hit points
    Shield's timer is now 5.
    Recharge provides 101 mana; its timer is now 2.
    '''
    assert player.hitpoints == 2
    assert player.armor == 7
    assert shield.timer == 5
    assert recharge.timer == 2
    '''
    Boss attacks for 8 - 7 = 1 damage!
    '''
    boss.attack(player)

    '''
    -- Player turn --
    - Player has 1 hit point, 7 armor, 211 mana
    - Boss has 14 hit points
    '''
    assert player.hitpoints == 1
    assert player.armor == 7
    assert player.mana == 211
    assert boss.hitpoints == 14
    turn(player, boss)
    '''
    Shield's timer is now 4.
    Recharge provides 101 mana; its timer is now 1.
    Player casts Drain, dealing 2 damage, and healing 2 hit points.
    '''
    assert recharge.timer == 1
    assert shield.timer == 4
    player_mana = player.mana
    drain = player.cast(Drain, boss)
    assert drain not in player.spells
    assert drain not in boss.spells

    '''
    -- Boss turn --
    - Player has 3 hit points, 7 armor, 239 mana
    - Boss has 12 hit points
    '''
    assert player.mana == 239
    assert player.hitpoints == 3
    assert boss.hitpoints == 12
    '''
    Shield's timer is now 3.
    Recharge provides 101 mana; its timer is now 0.
    Recharge wears off.
    '''
    turn(player, boss)
    assert shield.timer == 3
    assert recharge.timer == 0
    assert recharge not in player.spells
    '''
    Boss attacks for 8 - 7 = 1 damage!
    '''
    boss.attack(player)
    '''
    -- Player turn --
    - Player has 2 hit points, 7 armor, 340 mana
    - Boss has 12 hit points
    '''
    assert player.mana == 340
    assert player.hitpoints == 2
    assert boss.hitpoints == 12
    assert shield.timer == 3

    '''
    Shield's timer is now 2.
    '''
    turn(player, boss)
    assert shield.timer == 2
    '''
    Player casts Poison.
    '''
    poison = player.cast(Poison, boss)
    '''
    -- Boss turn --
    - Player has 2 hit points, 7 armor, 167 mana
    - Boss has 12 hit points
    Shield's timer is now 1.
    Poison deals 3 damage; its timer is now 5.
    '''
    turn(player, boss)
    assert player.mana == 167
    assert player.armor == 7
    assert player.hitpoints == 2
    assert boss.hitpoints == 9
    assert poison.timer == 5
    assert shield.timer == 1
    '''
    Boss attacks for 8 - 7 = 1 damage!
    '''
    boss.attack(player)

    '''
    -- Player turn --
    - Player has 1 hit point, 7 armor, 167 mana
    - Boss has 9 hit points
    Shield's timer is now 0.
    Shield wears off, decreasing armor by 7.
    Poison deals 3 damage; its timer is now 4.
    '''
    turn(player, boss)
    assert shield.timer == 0
    assert shield not in player.spells
    assert player.armor == 0
    '''
    Player casts Magic Missile, dealing 4 damage.
    '''
    player.cast(MagicMissile, boss)
    assert boss.hitpoints == 2
    
    '''
    -- Boss turn --
    - Player has 1 hit point, 0 armor, 114 mana
    - Boss has 2 hit points
    Poison deals 3 damage. This kills the boss, and the player wins.
    '''
    turn(player, boss)
    assert player.hitpoints == 1
    assert player.mana == 114
    assert player.armor == 0
    assert boss.hitpoints == -1
