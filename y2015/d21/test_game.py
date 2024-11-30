try:
    import game, shop, character, build, shop_item
except:
    from . import game, shop, character, build, shop_item

def test_get_buids():
    s = shop.Shop()
    builds = list(game.get_builds(s))
    assert len(builds) == 1260

    for b in builds:
        assert b.lring is not b.rring
        assert b.lring != b.rring

def test_game():
    boss = character.Character.from_file('boss')
    print(boss)
    player = character.Character('player', 100, 0, 0)
    print(player)
    b = build.Build(
        shop_item.Weapon('Weapons', 'sword', 10, 10, 0, 1),
        shop_item.Weapon('Armors', 'armor', 10, 0, 10, 1),
        shop_item.Weapon('Rings', 'left ring', 10, 1, 0, 1),
        shop_item.Weapon('Rings', 'right ring', 10, 0, 1, 1)
    )
    player.equip(b)
    winner = game.fight(player, boss)
    print(boss)
    print(player)
    assert winner is player
    assert player.hitpoints == 90
    assert boss.hitpoints == -6
    
