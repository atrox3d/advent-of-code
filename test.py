from pathlib import Path
import json
import csv
import logging
import types

logger = logging.getLogger(__name__)


def test(
            module:types.ModuleType,
            target_path:Path|str, 
            # input1_filename:str,
            # input2_filename:str,
            test_filename:str=None,
            expected=None
    ):
    logger.info(f'running {target_path!s}')
    if not target_path.exists():
        raise FileNotFoundError(f'target path not found: {target_path}')


    # Verify contents of the module:
    # print(dir(module))
    logger.info('running module.test')
    try:
        module.test(
                        target_path, 
                        # input1_filename, 
                        # input2_filename, 
                        test_filename,
                        expected
                    )
    except Exception as e:
        logger.error(e)
        raise
    logger.info('end run module.test')