from string import ascii_lowercase

forbidden = 'iol'
valid = ''.join(char for char in ascii_lowercase if char not in forbidden)

def check_straight(string: str, valid: str, length: int=3) -> bool:
    '''
    Passwords must include one increasing straight of at least 
    three letters, like abc, bcd, cde, and so on, up to xyz. 
    They cannot skip letters; abd doesn't count.
    '''
    print(string)
    for pos, _ in enumerate(string + ' '*length):
        t = string[pos:pos+length]
        if t in valid:
            return True
    return False

