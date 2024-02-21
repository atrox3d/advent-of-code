def sub_range (n):
    if n == 0:              # base case
        return [0]
    
    ret = sub_range(n-1)     # towards base case
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
