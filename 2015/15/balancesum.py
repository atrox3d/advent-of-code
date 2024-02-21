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

print(subrange(5))
print(add_range(3))

def rng(start, end):
    if start - end == 0:
        return []
    # if end - start > 0:
        # 
    # else:
        
