import logging
from string import ascii_lowercase

try:
    from valid import valid_chars
except:
    from .valid import valid_chars

logger = logging.getLogger(__name__)

def rincrement(password: str, valid_chars: str=ascii_lowercase) -> str:
    '''
    Incrementing is just like counting with numbers: 
    xx, xy, xz, ya, yb, and so on. 
    Increase the rightmost letter one step; 
    if it was z, it wraps around to a, and repeat with the 
    next letter to the left until one doesn't wrap around.
    '''
    logger.debug(f'{password = }')
    if password == '':
        return ''
    char = newchar = password[-1]
    partition = valid_chars.partition(char)
    logger.debug(f'{partition = }')
    partition = valid_chars.partition(char)[-1]
    if partition:
        newchar = partition[0]
        logger.debug(f'return {password[:-1] + newchar}')
        return password[:-1] + newchar
    else:
        newchar = valid_chars[0] # a
        ret = rincrement(password[:-1], valid_chars)
        logger.debug(f'return {ret + newchar}')
        return ret + newchar


if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    logger.setLevel('DEBUG')
    print(rincrement('ghizzzzz'))
    print(rincrement('aaaaaaaa'))
