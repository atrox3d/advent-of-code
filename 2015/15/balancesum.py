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
        if direction < 0:
            end, start = start, end

    print(f'{start, end, direction = }')
    if end == start:
        yield end
    else:
        ret = rng(start, end -1, direction)
        print(f'{ret = }')
        for val in ret:
            print(f'{val = }')
            if direction > 0:
                # print(f'yield {val=} + {[end]=}')
                # yield val + [end]
                for r in [val] + [end]:
                    print(f'yield {r=}')
                    yield r
            elif direction < 0:
                # yield [end] + val
                for r in [end] + [val]:
                    print(f'yield {r=}')
                    yield r
            else:
                yield []


# print(subrange(5))
# print(add_range(3))

# print(rng(0, 2))
# print(rng(2, 0))
for x in rng(0, 2): print(f'{x = }')