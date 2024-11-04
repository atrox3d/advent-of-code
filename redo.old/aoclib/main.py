import logging
from pathlib import Path

from .helpers import datainput
from .testing import testing
from .helpers import parse

logger = logging.getLogger(__name__)

def process_inputfile(solution, input_path):
        quiz_input = datainput.get_input(input_path)
        logger.info('running solution')
        result = solution(quiz_input)
        logger.info(f'{result = }')

def process_inputparam(solution, input_param):
    logger.info('running solution from parameter')
    logger.info(f'{input_param = }')
    result = solution(input_param)
    logger.info(f'{result = }')

def test_inputparam(solution, test_input, test_expected):
    logger.info('testing solution from parameters:')
    logger.info(f'{test_input = }')
    logger.info(f'{test_expected = }')
    result = solution(test_input)
    logger.info(f'{result = }')
    if test_expected is not None:
        '''
        check result against test_expected, if present
        '''
        try:
            assert result == test_expected, f'FAIL: {result} != {test_expected}'
            print(f'PASS: {test_input = } {result} == {test_expected}')
        except AssertionError as ae:
            print(repr(ae))


def main(
            solution, 
            input_param=None, 
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
    parse.log_cmdline_options(options)

    if input_param is not None:
        #  use parameter as input value
        process_inputparam(solution, input_param)

    elif test_input is not None:
        #  use parameter as test input value
        test_inputparam(solution, test_input, test_expected)
    
    elif options.test_param:
        # TODO: verify
        raise NotImplementedError('TODO: implement test_param correctly')
        logger.info(f'testing solution against {options.test_param}')
        testing.test_param(solution, options.test_param, options.input_path)
    
    elif options.test_path:
        # test solution again tests inside 
        test_path = Path(options.test_path)
        if not test_path.exists() and not test_path.is_absolute():
            test_path = testing.TESTS_DIR / test_path.name
            logger.warning(f'fixing test input path: {test_path = }')
        
        logger.info(f'testing solution against tests')
        testing.test_solution(solution, expected=options.expected, input_path=test_path) 

    elif options.print:
        # prints input and exit
        quiz_input = datainput.get_input(options.input_path)
        logger.info(f'printing input')
        datainput.print_input(quiz_input)

    elif options.input_path:
        # DEFAULT process input
        process_inputfile(solution, options.input_path)
    else:
        raise ValueError(f'check parser: {options = }')
