import logging

from .helpers import datainput
from .testing import testing
from .helpers import parse

logger = logging.getLogger(__name__)

def main(
            solution, 
            input=None, 
            test_input=None,
            test_expected=None, 
            level='DEBUG', 
            **loggerargs,
    ):
    logging.basicConfig(
                level=level, 
                format='%(levelname)5.5s|%(module)10.10s|%(funcName)15.15s| %(message)s',
                **loggerargs
                )
    options = parse.get_parser().parse_args()
    logger.debug(f'{options = }')
    parse.log_options(options)

    if input is not None:
        logger.info('running solution from parameter')
        logger.info(f'{input = }')
        result = solution(input)
        logger.info(f'{result = }')

    elif test_input is not None:
        logger.info('testing solution from parameter')
        logger.info(f'{test_input = }')
        logger.info(f'{test_expected = }')
        result = solution(test_input)
        logger.info(f'{result = }')
        if test_expected is not None:
            assert result == test_expected, f'FAIL: {result} != {test_expected}'
            print(f'PASS: {result} == {test_expected}')
    
    elif options.test_param:
        logger.info(f'testing solution against {options.test_param}')
        testing.test_param(solution, options.test_param,
                         options.input_path)
    
    elif options.test:
        logger.info(f'testing solution against tests')
        testing.test_solution(solution, input_path=options.test) 

    elif options.print:
        quiz_input = datainput.get_input(options.input_path)
        logger.info(f'printing input')
        datainput.print_input(quiz_input)

    else:
        quiz_input = datainput.get_input(options.input_path)
        logger.info('running solution')
        result = solution(quiz_input)
        logger.info(f'{result = }')
