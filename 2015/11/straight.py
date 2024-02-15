from string import ascii_lowercase
import logging

logger = logging.getLogger(__name__)

forbidden = 'iol'
valid = ''.join(char for char in ascii_lowercase if char not in forbidden)

def has_straight(string: str, valid: str, length: int=3) -> bool:
    '''
    Passwords must include one increasing straight of at least 
    three letters, like abc, bcd, cde, and so on, up to xyz. 
    They cannot skip letters; abd doesn't count.
    '''
    # logger.debug(string)
    for pos, _ in enumerate(string + ' '*length):
        pattern = string[pos:pos+length]
        logger.debug(f'{pattern = }')
        if pattern in valid:
            return True
    return False

