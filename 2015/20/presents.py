def get_house(target, max_houses):
    ''' returns the first house with presents >= target '''

    presents = [0] * max_houses             # create arrays of 0
    for house in range(1, max_houses+1):    # loop over every house, ignore 0
        elf = house                         # start with next elf
        while elf < max_houses:             
            presents[elf] += 10 * house     # update presents in multiple house
            elf += house                    # got through all multiple houses
        if presents[house] >= target:
            return house, presents[house]

def get_presents_per_house(house:int) -> int:
    ''' return total presents for this house '''

    return sum(filter(lambda elf: house%elf==0, range(1, house+1))) * 10

if __name__ == '__main__':
    max_houses = 1_000_000
    target = 33_100_000

    house, presents = get_house(target, max_houses)
    print(f'{house=:_}, {presents=:_}')

    presents_per_house = get_presents_per_house(house)
    print(f'{presents_per_house=:_}')

