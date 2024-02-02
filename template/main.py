import sys
import logging

import helpers
import tests

logging.basicConfig(level='DEBUG')
logger = logging.getLogger(__name__)

def solution(quiz_input):
    """
    """
    helpers.print_input(quiz_input)
    return False

if __name__ == '__main__':
    if sys.argv[1:]:
        param = sys.argv[1]
        logger.info(f'param detected:')
        if param.lower() == 'test':
            logger.info(f'testing solution against tests')
            tests.test(solution)
        else:
            logger.info(f'testing solution against {param}')
            tests.test_param(solution, param)
    else:
        quiz_input = helpers.get_input()
        logger.info('running solution')
        result = solution(quiz_input)
        logger.info(f'{result = }')
