def rincrement(password: str, valid: str) -> str:
    incremented = _rincrement(password[::-1], valid)[::-1]
    return incremented

def _rincrement(password: str, valid_chars) -> str:
    '''
    Incrementing is just like counting with numbers: 
    xx, xy, xz, ya, yb, and so on. 
    Increase the rightmost letter one step; 
    if it was z, it wraps around to a, and repeat with the 
    next letter to the left until one doesn't wrap around.
    '''
    if password == '':
        return ''
    char = newchar = password[0]
    partition = valid_chars.partition(char)[-1]
    if partition:
        newchar = partition[0]
        return newchar + password[1:]
    else:
        newchar = valid_chars[0] # a
        return newchar + _rincrement(password[1:], valid_chars)
