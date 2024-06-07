def cansum(targetsum: int, numbers: list, memo: dict=None) -> bool:
    '''
    write a function cansum(targetsum, numbers) that takes in a
    targetsum and an array of numbers as arguments

    the function should return a boolelan indicating wether
    or not it is possible to generate the targetsum using the
    numbers in the array

    you may use an element of the array asm many times as needed

    you may assume that all input numbers are nonnegative
    '''
    memo = {} if memo is None else memo
    try:
        ret = memo[targetsum]
        return memo[targetsum]
    except:
        pass

    if targetsum == 0:
        return True
    
    if targetsum < 0:
        return False

    for number in numbers:
        ret = cansum(targetsum-number, numbers, memo)
        try:
            memo[targetsum] = ret
        except:
            pass
        if ret == True:
            return ret
    return False

if __name__ == '__main__':

    data = (
        (25, [20, 15, 10, 5, 5]),
        # (7, [2, 3]),
        # (7, [5, 3, 4, 7]),
        # (7, [2, 4]),
        # (8, [2, 3, 5]),
    )

    for targetsum, numbers in data:
        outer_memo = {}
        result = cansum(targetsum, numbers, outer_memo)
        print(f'{targetsum = }')
        print(f'{numbers = }')
        print(f'{result = }')
        print(f'{outer_memo = }')
        print()