from pathlib import Path
import json
import csv
import logging
import types

logger = logging.getLogger(__name__)


def run(
            module:types.ModuleType,
            target_path:Path|str, 
            # python_filename:str,
            input1_filename:str,
            # expected1,
            input2_filename:str,
            # expected2,
    ):
    logger.info(f'running {target_path!s}')
    if not target_path.exists():
        raise FileNotFoundError(f'target path not found: {target_path}')


    # Verify contents of the module:
    # print(dir(module))
    logger.info('running module.main')
    try:
        module.main(
                        target_path, 
                        input1_filename, 
                        # expected1, 
                        input2_filename, 
                        # expected2
                    )
    except Exception as e:
        logger.error(e)
        raise
    logger.info('end run module.main')