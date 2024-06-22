target = 33_100_000
max_houses = 1_000_000

def get_house(target, max_houses):
    presents = [0] * max_houses             # create arrays of 0
    for house in range(1, max_houses+1):    # loop over every house
        tmp = house - 1                     # adjust index to zero based?

        while tmp < max_houses:             # 

            presents[tmp] += 10 * house

            tmp += house
        if presents[house - 1] >= target:
            print(f"Part 1: {house:_}")
            return house, presents[house-1]

def get_presents_per_house(house:int) -> int:
    return sum(filter(lambda elf: house%elf==0, range(1, house+1))) * 10


house, presents = get_house(target, max_houses)
print(f'{house=:_}, {presents=:_}')

presents_per_house = get_presents_per_house(house)
print(f'{presents_per_house=:_}')

