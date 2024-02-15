import logging

logger = logging.getLogger(__name__)


def increment(password: str) -> str:
    '''
    Incrementing is just like counting with numbers: 
    xx, xy, xz, ya, yb, and so on. 
    Increase the rightmost letter one step; 
    if it was z, it wraps around to a, and repeat with the 
    next letter to the left until one doesn't wrap around.
    '''
    from string import ascii_lowercase
    # print(password)
    # print(password[::-1])
    newpassword = ''
    for pos, char in enumerate(password[::-1]):
        find = ascii_lowercase.index(char)
        try:
            new_char = ascii_lowercase[find+1]
            newpassword += new_char
            newpassword += password[::-1][pos+1:]
            break
        except IndexError:
            new_char = ascii_lowercase[0]
            newpassword += new_char
    
    # print (newpassword[::-1])
    return newpassword[::-1]


if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    logger.setLevel('DEBUG')
    print(increment('ghizzzzz'))