import logging
from valid import valid_chars
from string import ascii_lowercase

logger = logging.getLogger(__name__)

def rincrement(password: str, valid: str=ascii_lowercase) -> str:
    incremented = _rincrement(password[::-1], valid)[::-1]
    return incremented

def _rincrement(password: str, valid_chars: str) -> str:
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
    char = newchar = password[0]
    partition = valid_chars.partition(char)
    logger.debug(f'{partition = }')
    partition = valid_chars.partition(char)[-1]
    if partition:
        newchar = partition[0]
        logger.debug(f'return {newchar + password[1:]}')
        return newchar + password[1:]
    else:
        newchar = valid_chars[0] # a
        ret = _rincrement(password[1:], valid_chars)
        logger.debug(f'return {newchar + ret}')
        return newchar + ret


if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    logger.setLevel('DEBUG')
    print(rincrement('ghizzzzz', ascii_lowercase))