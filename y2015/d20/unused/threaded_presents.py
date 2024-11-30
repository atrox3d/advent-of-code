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

########################################################################
# test functions againsta example values
########################################################################
def test_base_logic(start:int, end:int, examples:list, compute:Callable[[int], int],
                    print_success:bool=True, print_failure:bool=True,
    ):
    ''' tests the base functions against the examples '''
    logic_ok = True
    for house in range(start, end+1):
        presents = compute(house)
        try:
            assert presents == examples[house]
            if print_success: print(f'SUCCESS | house {house}: {presents} == {examples[house]}')
        except AssertionError as ae:
            logic_ok = False
            if print_failure: print(f'FAIL    | house {house}: {presents} != {examples[house]}')
    return logic_ok

def brute_force(total:int, results:list[int]) -> int:
    house = 0
    presents = 0
    try:
        while presents < total:
            house += 1
            presents = get_presents_per_house(house)
        return house
    except KeyboardInterrupt:
        print(f'INTERRUPTED | {house=}, {presents=}, {total=}')
        exit()

import threading, time

def presents_thread(house, target, done, status):
    if not done[0]:
        presents = get_presents_per_house(house)
        # print(f'{house=:<10}, {target=:<10}, {presents=:<10}, {results=}')
        status['house'] = house
        status['presents'] = presents
        if presents >= target:
            done[0] = True
            results.append(presents)
    else:
        print(f'{done=} thread not running')

done = [False]
def no_join(function, house, target, done, status):
    # house = 1
    while not done[0]:
        try:
            th = threading.Thread(target=function, 
                                  args=(house, target, done, status))
            # print(f"starting thread {th.getName()}")
            # th.daemon = True
            th.start()
            # if house % 10_000 == 0:
                # print(f'{house = :_}')
                # print(f'{status['house']=:_}, {status['target']=:_}, {status['presents']=:_}')
            house += 1
        except KeyboardInterrupt:
            print(f'\n{results=}')
            print(f'{status['house']=:_}, {status['target']=:_}, {status['presents']=:_}')
            if input('exit (y/n)?') == 'y':
                break
    print(results)

if __name__ == '__main__':
    start=1
    end=9
    examples=[None, 10, 30, 40, 70, 60, 120, 80, 150, 130]
    assert test_base_logic(start, end, examples, compute=get_presents_per_house), f'failed logic check'

    total=10_0000
    total=33_100_000
    offset = 1000_000
    results = []
    status = {'target': total, 'house': 0, 'presents': 0}
    # result = brute_force(total)
    # print(result)
    # run_threads(presents_thread, total, results, condition=lambda:len(results)>0)
    no_join(presents_thread, 900_000, total, done, status)
