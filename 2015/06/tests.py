import helpers
import logging

logger = logging.getLogger(__name__)

def test_param(solution, param):
        if helpers.is_multiline(helpers.INPUT_PATH):
            logger.debug(f'converting {param} to list')
            param = [param]    
        print(solution(param))

def test(solution):
    tests = [
        {
            'input': None, 
            'expected': None,
        },
    ]
    for test in tests:
        _input = test['input']
        expected = test['expected']
        logger.info(f'testing {_input}: {expected=}')
        result = solution(test['input'])
        try:
            assert expected == result, f'{expected=} != {result=}'
            logger.info(f'PASS: {expected=} != {result=}')
        except AssertionError as ae:
            logger.error(f'FAIL: {expected=} != {result=}')
            # print(repr(ae))
        finally:
            print()
