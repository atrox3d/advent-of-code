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
