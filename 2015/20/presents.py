'''
House 1 got 10 presents.
House 2 got 30 presents.
House 3 got 40 presents.
House 4 got 70 presents.
House 5 got 60 presents.
House 6 got 120 presents.
House 7 got 80 presents.
House 8 got 150 presents.
House 9 got 130 presents.

The first house gets 10 presents: it is visited only by Elf 1, 
which delivers 1 * 10 = 10 presents. 

The fourth house gets 70 presents, because it is visited by Elves 
1, 2, and 4, for a total of 10 + 20 + 40 = 70 presents.

# 33100000
'''
from typing import Generator

def get_houses_for_elf(elf:int, here:int) -> Generator[int, None, None]:
    if here % elf != 0:
        raise ValueError
    return [house for house in range(elf, here+1, elf)]

def check_every_house(
        from_house=1, to_house=9, from_elf=None, to_elf=None
    ):
    from_elf = from_elf if from_elf is not None else from_house
    to_elf = to_elf if to_elf is not None else to_house

    for house in range(from_house, to_house+1):
        for elf in range(from_elf, to_elf+1):
            try:
                houses = get_houses_for_elf(elf, house)
                print(f'{house = }, {elf = }', houses) 
            except ValueError:
                pass
        print()

def get_elves_for_house(house:int) -> Generator[int, None, None]:
    return (elf for elf in range(1, house+1) if house % elf == 0)

def compute_presents(house:int, presents_per_elf=10):
    return sum(get_elves_for_house(house)) * presents_per_elf


for house in range(1, 9+1):
    print(house, compute_presents(house), list(get_elves_for_house(house)))
exit()
results = [None, 10, 30, 40, 70, 60, 120, 80, 150, 130]
for house in range(1, 10):
    presents = compute_presents(house)
    try:
        assert presents == results[house]
        print(f'SUCCESS | house {house}: {presents} == {results[house]}')
    except AssertionError as ae:
        print(f'FAIL    | house {house}: {presents} != {results[house]}')
