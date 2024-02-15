from string import ascii_lowercase

def rincrement(password: str, valid_chars) -> str:
    '''
    Incrementing is just like counting with numbers: 
    xx, xy, xz, ya, yb, and so on. 
    Increase the rightmost letter one step; 
    if it was z, it wraps around to a, and repeat with the 
    next letter to the left until one doesn't wrap around.
    '''
    print(f'{password = !r}')

    if password == '':
        return ''

    char = newchar = password[0]
    print(f'{char = }')
    partition = valid_chars.partition(char)[-1]
    print(f'{partition = }')
    if partition:
        newchar = partition[0]
        ret = newchar + password[1:]
        print(ret)
        return ret
    else:
        newchar = valid_chars[0] # a
        ret = newchar + rincrement(password[1:], valid_chars)
        print(ret)
        return ret
    # print(newchar)

# rincrement('zzz')
valid = ''.join(char for char in ascii_lowercase if char not in 'iol')
print(f'{valid = }')
result = rincrement('za'[::-1], valid)[::-1]
print(f'{result = }')