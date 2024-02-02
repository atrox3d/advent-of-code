import logging

import main

logging.basicConfig(
            level='DEBUG', 
            format='%(levelname)5.5s|%(module)12.12s|%(funcName)15.15s| %(message)s'
            )
logger = logging.getLogger(__name__)

def solution(quiz_input):
    """
    """
    return False

if __name__ == '__main__':
    main.main(solution)