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

def find_house_for_total_presents(
        total:int, 
        compute_presents:Callable[[int], int],
        first_house=1,
        offset=100
        ) -> int:
    '''
    loop over every house until the total presents match (?) total

    TOO SLOW for higher values

    not found curr_house = 613491, presents = 8832000, total = 33100000
    What is the lowest house number of the house to get at least as many 
    presents as the number in your puzzle input? # 33100000
    '''
    done = False
    curr_house = first_house
    len_total = len(str(total))
    while not done:
        presents = compute_presents(curr_house)
        # not likely
        if presents == total:
            print(f'FOUND {first_house:}->{curr_house:_}, {presents:_} <= {total:_} ')
            done = True
            # always
        elif presents <= total:
            # not enough
            if len(str(presents)) == len(str(total)):
                # same order, filter out too low/too high
                print(f'NOT FOUND {first_house:<10_}->{curr_house:>10_}, {presents:>12_} <= {total:<12_} ' 
                    f'{len(str(presents)):2} - {len(str(total)):2}')
                # print('.', end='', flush=True)
            curr_house += 1
        else:
            #
            # need to catch the lower greater than
            #
            # - same len is same order, filter out values too high
            #
            if len(str(presents)) == len_total:
                # - try to stay in a range/offset ti guess the lower greater than
                if (presents - total) <= offset:
                    print(f'    FOUND {first_house:<10_}->{curr_house:>10_}, '
                          f'{presents:<12_} >= {total:<12_} -- {offset=}')
                    done = True
                else:
                    # greater than but different order (len)
                    raise ValueError(f'{presents} > {total}')
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
            if print_success:
                print(f'SUCCESS | house {house}: {presents} == {results[house]}')
        except AssertionError as ae:
            logic_ok = False
            if print_failure:
                print(f'FAIL    | house {house}: {presents} != {results[house]}')
    return logic_ok

assert \
    test_base_logic(
        start_house=1,
        end_house=9,
        results=[None, 10, 30, 40, 70, 60, 120, 80, 150, 130],
        compute_presents=get_presents_per_house
        ), f'failed logic check'

def main(total:int, start:int, end:int, offset:int) -> int | list[int]:
    houses = []
    for limiter in range(start, end+1):
        first_house = total // limiter
        try:
            print(f'find: {total=} / {first_house=} / {limiter=} / {offset=}')
            house = find_house_for_total_presents(
                                    total=total, 
                                    compute_presents=get_presents_per_house,
                                    first_house=first_house,
                                    offset=offset
                                )
            houses.append(house)
            print(f'{house = }')
        except ValueError:
            print()
            print(f'FAILED with {limiter=}, {first_house=} {offset=}')
            print()
    return sorted(houses)

total=33_100_000
offset = 1000_000
