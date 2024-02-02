import helpers

import logging

logger = logging.getLogger(__name__)

def test_param(solution, param, multiline):
        if multiline:
            logger.debug(f'converting {param} to list')
            param = [param]
        return solution(param)

def test(solution, multiline):
    tests = [
        (None, None),
    ]

    for _input, expected in tests:
        logger.info(f'testing {_input}: {expected=}')
        result = test_param(solution, _input, multiline)
        try:
            assert expected == result, f'{expected=} != {result=}'
            logger.info(f'PASS: {expected=} != {result=}')
        except AssertionError as ae:
            logger.error(f'FAIL: {expected=} != {result=}')
            # print(repr(ae))
        finally:
            print()
