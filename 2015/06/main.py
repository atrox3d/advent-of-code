import logging

import helpers
import tests
import parse

logger = logging.getLogger(__name__)

def main(solution, level='DEBUG'):
    logging.basicConfig(
                level=level, 
                format='%(levelname)5.5s|%(module)12.12s|%(funcName)15.15s| %(message)s'
                )
    options = parse.get_parser().parse_args()
    # logger.debug(f'{options = }')
    parse.log_options(options)

    if options.test_param:
        logger.info(f'testing solution against {options.test_param}')
        tests.test_param(solution, options.test_param, 
                         helpers.is_multiline(input_path=options.input_path))
    
    elif options.test:
        logger.info(f'testing solution against tests')
        tests.test(solution, input_path=options.test, 
                   multiline=helpers.is_multiline(input_path=options.input_path))

    elif options.print:
        quiz_input = helpers.get_input(options.input_path)
        logger.info(f'printing input')
        helpers.print_input(quiz_input)

    else:
        quiz_input = helpers.get_input(options.input_path)
        logger.info('running solution')
        result = solution(quiz_input)
        logger.info(f'{result = }')
