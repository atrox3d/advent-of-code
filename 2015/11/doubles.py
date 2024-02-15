import logging

logger = logging.getLogger(__name__)

def has_doubles(string:str) -> bool:
    import re

    logger.debug(f'{string = }')

    redoubles = re.compile(r'([a-z])\1')
    redoubles = re.compile(r'([a-z])\1.*([a-z])\2')
    doubles = redoubles.search(string)
    # logger.debug(f'{doubles = }')

    if doubles is not None:
        prev = ''
        for item in doubles.groups():
            # logger.debug(f'{prev = }, {item = }')
            if prev == item:
                return False
            prev = item
        return True
    return False

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    logger.setLevel('DEBUG')
    print(has_doubles('abcdefgh'))
    print(has_doubles('ghjaaabb'))
    print(has_doubles('ghjaabcc'))