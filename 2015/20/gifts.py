def get_house(
                target:int, 
                max_houses:int, 
                gifts_per_elve:int=10,
                max_houses_per_elve:int=None,
    ) -> tuple[int, int]:
    ''' returns the first house with presents >= target '''

    presents = [0] * max_houses                         # create arrays of 0
    for house in range(1, max_houses+1):                # loop over every house, ignore 0
        elf = house                                     # start with next elf
        count = 1
        while elf < max_houses:             
            presents[elf] += gifts_per_elve * house     # update presents in multiple house
            elf += house                                # got through all multiple houses
            count += 1
            if max_houses_per_elve is not None:
                if count >= max_houses_per_elve:
                    break
        if presents[house] >= target:
            return house, presents[house]


def infinite_numbers():
    number = 1
    while True:
        yield number
        number += 1

def get_house_dict(target:int, gifts=10):
    elf = 1
    house = 1
    houses = {}
    for house in infinite_numbers():
        presents = 0
        if house > target:
            break
        for elf in range(1, house+1):
            if house%elf == 0:
                presents += (elf*gifts)
                yield house, elf, presents
        yield ' ', ' ', ' '

def get_presents_per_house(house:int) -> int:
    ''' return total presents for this house '''

    return sum(
            filter(
                lambda elf: house%elf==0, 
                range(1, house+1)
            )
        ) * 10



if __name__ == '__main__':
    max_houses = 1_000_000
    target = 33_100_000

    house, presents = get_house(target, max_houses, 11, 50)
    print(f'{house=:_}, {presents=:_}')

    presents_per_house = get_presents_per_house(house)
    print(f'{presents_per_house=:_}')

