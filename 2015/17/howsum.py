def howsum(targetsum: int, numbers: list, memo=None) -> list:
    '''
    write a function howsum(targetsum, numbers) that takes in a
    targetsum and an array of numbers as arguments

    the function should return an array containing any combination
    elements that add up to exactly the targetsum.
    if there is no combination that satisfies, then return null

    if there are multiple combinations possible, you may
    return any single one

    brute force:
    time: O(len(numbers)^targetsum * targetsum)
    space: O(targetsum)
    
    momoized:
    # polynomial, not exponential, because exponent is constant
    time: O(len(numbers) * targetsum^2)
    # quadratic complexity
    space: O(targetsum^2)
    '''
    memo = {} if memo is None else memo # init memo dict
    try:
        return memo[targetsum]          # try to return cached result
    except Exception as e: pass

    if targetsum == 0: return []        # job is complete

    if targetsum < 0: return None       # failed
    
    for num in numbers:
        ret = howsum(targetsum-num, numbers, memo)
        if ret is not None:
            # try:
            memo[targetsum] = ret + [num]
            # except Exception as e: pass
            return ret + [num]
    
    # try:
    memo[targetsum] = None
    # except Exception as e: pass
    return None

if __name__ == '__main__':

    data = (
        (25, [20, 15, 10, 5, 5]),
        # (7, [2, 3]),
        # (7, [5, 3, 4, 7]),
        # (7, [2, 4]),
        # (8, [2, 3, 5]),
        # (300, [7, 14]),
    )

    for targetsum, numbers in data:
        outer_memo = {}
        print(f'INPUT | {targetsum = }')
        print(f'INPUT | {numbers = }')
        result = howsum(targetsum, numbers, outer_memo)

        print(f'{result = }')
        print(f'{outer_memo = }')
        assert result is None or sum(result) == targetsum
        print()
