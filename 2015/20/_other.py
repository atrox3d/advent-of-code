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

'''
def factorial(number):
    if number == 1:
        return 1
    
    return number * factorial(number -1)

def fib(n: int, cache=None) -> int:
    cache = {} if cache is None else cache
    if n in (0, 1):
        return n
    
    if cache is not None:
        try:
            return cache[n]
        except KeyError:
            cache[n] = fib(n-1, cache) + fib(n-2, cache)
            return cache[n]
    else:
        ret = fib(n-1, cache) + fib(n-2, cache)
        return ret

def deliver(presents:str) -> int:
    if isinstance(presents, str):
        presents = int(presents.strip())
    return presents

# 33100000
