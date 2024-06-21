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

def get_presents_per_house(house:int) -> int:
    return sum(filter(lambda elf: house%elf==0, range(1, house+1))) * 10

def find_house_for_total_presents(total:int, compute_presents:Callable[[int], int]) -> int:
    '''
    loop over every house until the total presents match (?) total

    TOO SLOW for higher values

    not found curr_house = 613491, presents = 8832000, total = 33100000
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

########################################################################
# test functions againsta example values
########################################################################
def test_base_logic(
        start_house:int, 
        end_house:int, 
        results:list, 
        compute_presents:callable,
        print_success=True,
        print_failure=True,
    ):
    ''' tests the base functions against the examples '''

    logic_ok = True
    for house in range(start_house, end_house+1):
        presents = compute_presents(house)
        try:
            assert presents == results[house]
            print(f'SUCCESS | house {house}: {presents} == {results[house]}')
        except AssertionError as ae:
            print(f'FAIL    | house {house}: {presents} != {results[house]}')
            logic_ok = False
    return logic_ok


start_house = 1
end_house = 9
results = [None, 10, 30, 40, 70, 60, 120, 80, 150, 130]

assert \
    test_base_logic(
        start_house,
        end_house,
        results,
        get_presents_per_house
        ), f'failed logic check'