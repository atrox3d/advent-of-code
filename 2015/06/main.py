import sys
import logging

import helpers
import tests

logging.basicConfig(level='DEBUG', format='%(levelname)5.5s|%(module)12.12s|%(funcName)15.15s| %(message)s')
logger = logging.getLogger(__name__)

def solution(quiz_input):
    """
    """
    return False

if __name__ == '__main__':
    if sys.argv[1:]:
        param = sys.argv[1]
        logger.info(f'param detected: {param!r}')
        if param.lower() == 'test':
            logger.info(f'testing solution against tests')
            tests.test(solution)
        elif param.lower() == 'print':
            quiz_input = helpers.get_input()
            logger.info(f'printing input')
            helpers.print_input(quiz_input)
        else:
            logger.info(f'testing solution against {param}')
            tests.test_param(solution, param)
    else:
        quiz_input = helpers.get_input()
        logger.info('running solution')
        result = solution(quiz_input)
        logger.info(f'{result = }')
