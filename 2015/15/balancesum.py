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
    return ret   + [n]
    # or
    # return [*ret] + [n]
    
    # normal
    #       1    [0]
    #       2    [1,0]
    #       3    [2,1,0]
    return [n] + ret
    # or
    # return [n] + [*ret]

def y (n, k=0):
    if k == n:
        return []
    
    ret = y(n, k+1)
    print(ret)  # [0], [1, 0], [2, 1, 0], ...
    return [k] + ret

print(subrange(5))
# print(y(7))

def rng(start, end):
    if start - end == 0:
        return []
    # if end - start > 0:
        # 
    # else:
        
