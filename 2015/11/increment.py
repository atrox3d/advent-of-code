import logging
from string import ascii_lowercase

logger = logging.getLogger(__name__)


def increment(password: str, valid_chars: str=ascii_lowercase) -> str:
    '''
    Incrementing is just like counting with numbers: 
    xx, xy, xz, ya, yb, and so on. 
    Increase the rightmost letter one step; 
    if it was z, it wraps around to a, and repeat with the 
    next letter to the left until one doesn't wrap around.
    '''
    newpassword = ''
    for pos, char in enumerate(password[::-1]):
        find = valid_chars.index(char)
        try:
            new_char = valid_chars[find+1]
            newpassword += new_char
            newpassword += password[::-1][pos+1:]
            break
        except IndexError:
            new_char = valid_chars[0]
            newpassword += new_char
    
    return newpassword[::-1]


if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    logger.setLevel('DEBUG')
    print(increment('ghizzzzz'))