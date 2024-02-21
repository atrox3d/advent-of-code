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
