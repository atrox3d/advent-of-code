def rincrement(password: str) -> str:
    '''
    Incrementing is just like counting with numbers: 
    xx, xy, xz, ya, yb, and so on. 
    Increase the rightmost letter one step; 
    if it was z, it wraps around to a, and repeat with the 
    next letter to the left until one doesn't wrap around.
    '''
    from string import ascii_lowercase

    if password == '':
        print()
        return ''
    print(f'{password = }')
    print(f'{password[0] = }')
    print(f'{password[1:] = }')
    ret = rincrement(password[1:])
    print(f'{ret = }, {password[0] = }')

    if ret == '':
        pass
    return  ret + password[0]
