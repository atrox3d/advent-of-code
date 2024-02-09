import logging

from .helpers import datainput
from . import tests
from . import parse

logger = logging.getLogger(__name__)

def main(solution, level='DEBUG', **loggerargs):
    logging.basicConfig(
                level=level, 
                format='%(levelname)5.5s|%(module)10.10s|%(funcName)15.15s| %(message)s',
                **loggerargs
                )
    options = parse.get_parser().parse_args()
    logger.debug(f'{options = }')
    parse.log_options(options)

    if options.test_param:
        logger.info(f'testing solution against {options.test_param}')
        tests.test_param(solution, options.test_param,
                         options.input_path)
    
    elif options.test:
        logger.info(f'testing solution against tests')
        tests.test_solution(solution, input_path=options.test) 

    elif options.print:
        quiz_input = datainput.get_input(options.input_path)
        logger.info(f'printing input')
        datainput.print_input(quiz_input)

    else:
        quiz_input = datainput.get_input(options.input_path)
        logger.info('running solution')
        result = solution(quiz_input)
        logger.info(f'{result = }')
