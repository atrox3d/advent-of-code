from string import ascii_lowercase
import logging

logger = logging.getLogger(__name__)

forbidden = 'iol'
valid = ''.join(char for char in ascii_lowercase if char not in forbidden)

def has_straight(
            string: str, 
            # valid: str, 
            length: int=3
    ) -> bool:
    '''
    Passwords must include one increasing straight of at least 
    three letters, like abc, bcd, cde, and so on, up to xyz. 
    They cannot skip letters; abd doesn't count.
    '''
    logger.debug(f'{string = }')
    for pos, _ in enumerate(string):
        pattern = string[pos:pos+length]
        if len(pattern) == length: 
            logger.debug(f'{pattern = }')
            index = ascii_lowercase.index(_)
            target = ascii_lowercase[index:index+length]
            if  target == pattern:
                return True
    return False

# if __name__ == '__main__':
#     logging.basicConfig(level='DEBUG')
#     logger.setLevel('DEBUG')
#     for string in ['abcdffaa', 'ghjaabcc', 'cqjxkkaa']:
#         print(has_straight(string, valid))
