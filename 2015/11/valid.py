import logging
from string import ascii_lowercase


from straight import has_straight
from doubles import has_doubles

logger = logging.getLogger(__name__)

forbidden = 'iol'
valid_chars = ''.join(char for char in ascii_lowercase if char not in forbidden)


def is_valid(string:str, valid_chars=valid_chars, forbidden=forbidden) -> bool:
    logger.debug(f'isvalid: {string}')
    if not has_doubles(string):
        logger.debug(f'{string} not has_doubles')
        return False
    if not has_straight(string, valid_chars):
        logger.debug(f'{string} not has_straight')
        return False
    for ch in string:
        if ch in forbidden:
            logger.debug(f'{string} has forbidden')
            return False
    logger.info(f'valid! {string}')
    return True

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    logger.setLevel('DEBUG')
    print(is_valid('ghjaabcc'))