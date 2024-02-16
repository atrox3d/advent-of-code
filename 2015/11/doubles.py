import logging

logger = logging.getLogger(__name__)

def has_doubles(string:str) -> bool:
    import re

    logger.debug(f'{string = }')

    redoubles = re.compile(r'([a-z])\1.*([a-z])\2')
    doubles = redoubles.search(string)
    logger.debug(f'{doubles = }')

    if doubles is not None:
        logger.debug(f'{doubles.groups() = }')
        for char in doubles.groups():

            if string.count(char*2) != 1:
                return False
            
            if string.count(char*3) != 0:
                return False 
       
        return True
    return False

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    logger.setLevel('DEBUG')
    print(has_doubles('abcdefgh'))
    print(has_doubles('ghjaaabb'))
    print(has_doubles('gjaaabcc'))
    print(has_doubles('abcdffaa'))
    print(has_doubles('ghjaabcc'))
    print(has_doubles('gjaabbcd'))