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

What is the lowest house number of the house to get at least as many 
presents as the number in your puzzle input? # 33100000
'''
from typing import Generator, Callable


def elves_per_house(house:int) -> list:
    return [elf for elf in filter(lambda elf: house % elf == 0, range(1, house+1))]

def presents_per_house(
                    house:int, 
                    compute_elves:Callable[[int], list[int]], 
                    presents_per_elf=10
    ) -> int:
    return sum(compute_elves(house)) * presents_per_elf

########################################################################

def get_presents_per_house(house:int) -> int:
    '''
    What is the lowest house number of the house to get at least as many 
    presents as the number in your puzzle input? # 33100000
    '''
    total = 0
    for elf in range(house, 0, -1):
        if house % elf == 0:
            total += elf * 10
    # print(f'total presents for {house = } : {total}')
    return total

########################################################################

def get_elves_for_house(house:int) -> Generator[int, None, None]:
    ''' generates all elves that will visit a house '''
    return (elf for elf in range(1, house+1) if house % elf == 0)

def compute_presents(house:int, presents_per_elf=10):
    ''' returns the total present for this house '''
    return sum(get_elves_for_house(house)) * presents_per_elf

########################################################################

def test_base_logic(
        start_house:int, 
        end_house:int, 
        results:list, 
        compute_presents:callable,
        *args,
        **kwargs
    ):
    ''' tests the base functions against the examples '''
    logic_ok = True
    for house in range(start_house, end_house+1):
        presents = compute_presents(house, *args, **kwargs)
        try:
            assert presents == results[house]
            print(f'SUCCESS | house {house}: {presents} == {results[house]}')
        except AssertionError as ae:
            print(f'FAIL    | house {house}: {presents} != {results[house]}')
            logic_ok = False
    return logic_ok

#########################################################################

def find_house_for_total_presents(total:int) -> int:
    '''
    TOO SLOW for higher values
    # not found curr_house = 613491, presents = 8832000, total = 33100000
    What is the lowest house number of the house to get at least as many 
    presents as the number in your puzzle input? # 33100000
    '''
    done = False
    curr_house = 1
    while not done:
        presents = compute_presents(curr_house)
        if presents == total:
            print(f'found {curr_house = }, {presents = }, {total = }')
            done = True
        else:
            print(f'not found {curr_house = }, {presents = }, {total = }')
            curr_house += 1
    return curr_house


start_house = 1
end_house = 9
results = [None, 10, 30, 40, 70, 60, 120, 80, 150, 130]
base_params = start_house, end_house, results

assert \
    test_base_logic(*base_params, get_presents_per_house), \
    f'failed logich check'

assert \
    test_base_logic(*base_params, compute_presents), \
    f'failed logich check'
