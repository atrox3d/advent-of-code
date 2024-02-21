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

verbose = True
def vprint(*args, **kwargs):
    if verbose:
        print(*args, **kwargs)

def rng(start, end, direction=None):
    if direction is None:
        direction = (end-start) // abs(end-start)
        if direction < 0:
            end, start = start, end

    vprint(f'{start, end, direction = }')
    if end == start:
        yield end
    else:
        ret = rng(start, end -1, direction)
        vprint(f'{ret = }')
        for val in ret:
            vprint(f'{val = }')
            if direction > 0:
                for r in [val] + [end]:
                    vprint(f'yield {r=}')
                    yield r
            elif direction < 0:
                for r in [end] + [val]:
                    vprint(f'yield {r=}')
                    yield r
            # else:
                # yield []


# print(subrange(5))
# print(add_range(3))

# print(rng(0, 2))
# print(rng(2, 0))
for x in rng(0, 2): print(f'{x = }')
print()
for x in rng(2, 0): print(f'{x = }')