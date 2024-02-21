'''
3   0 0 0
    3 0 0
    2 1 0
    1 2 0
    0 3 0
    0 2 1
    0 1 2
    0 0 3
'''
def subrange (n):
    if n == 0:              # base case
        return [0]
    
    ret = subrange(n-1)     # towards base case
    # reverse
    #      [0]      1
    #      [0,1]    2
    #      [0,1,2]  3
    return ret   + [n]      # or return [*ret] + [n]
    
    # normal
    #       1    [0]
    #       2    [1,0]
    #       3    [2,1,0]
    return [n] + ret        # or return [n] + [*ret]

def add_range (n, start=0):
    if start == n:
        return []                   # base case
    
    ret = add_range(n, start+1)     # towards base case
    print(ret)  # [0], [1, 0], [2, 1, 0], ...
    # normal
    #         2      []
    #         1      [2]
    #         0      [1,2]
    return [start] + ret    # or [start] + [*ret]
    # reverse
    #      []     2
    #      [2]    1
    #      [2,1]  0
    return ret + [start]    # or [*ret] + [start]

def rng(start, end, direction=None):
    if direction is None:
        direction = (end-start) // abs(end-start)

    if end == start:
        print(f'{start, end, direction = }')
        return [end]

    ret = rng(start, end-1, direction)
    if direction > 0:
        return ret + [end]
    elif direction < 0:
        return [end] + ret
    else:
        return []


# print(subrange(5))
# print(add_range(3))

print(rng(0, 2))
print(rng(2, 0))