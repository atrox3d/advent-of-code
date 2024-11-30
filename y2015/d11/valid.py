import logging
from string import ascii_lowercase


try:
    from straight import has_straight
    from doubles import has_doubles
except:
    from .straight import has_straight
    from .doubles import has_doubles

logger = logging.getLogger(__name__)

forbidden = 'iol'
valid_chars = ''.join(char for char in ascii_lowercase if char not in forbidden)

def check_chars(string:str, allowed=valid_chars, forbidden=forbidden) -> bool:
    for ch in string:
        if ch not in allowed or ch in forbidden:
            return False
    return True

def is_valid(string:str, valid_chars=valid_chars, forbidden=forbidden) -> bool:
    logger.debug(f'isvalid: {string}')

    if not has_doubles(string):
        logger.debug(f'FAIL: {string} ! has_doubles')
        return False
    logger.debug(f'OK: {string} has_doubles')

    if not has_straight(
                string, 
                # valid_chars
            ):
        logger.debug(f'FAIL: {string} ! has_straight')
        return False
    logger.debug(f'OK: {string} has_straight')

    # for ch in string:
    #     if ch in forbidden:
    #         logger.debug(f'FAIL: {string} has forbidden')
    #         return False
    if not check_chars(string, valid_chars, forbidden):
        return False
    
    logger.debug(f'OK: {string} ! has forbidden')
    logger.info(f'OK: valid! {string}')
    return True

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    logger.setLevel('DEBUG')
    for string in [
        # 'abcdffaa', 
        'gjaabbcd', 
        'ghjaabcc',
        ]:
        print(is_valid(string))
        print()