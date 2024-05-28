from pathlib import Path
import json
import csv
import logging
import importlib.util
import types

logger = logging.getLogger(__name__)

def load_module(target_path:Path, python_filename:str) -> types.ModuleType:
    file_path = target_path / python_filename
    module_name = file_path.stem

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def run(
            target_path:Path|str, 
            python_filename:str,
            input1_filename:str,
            # expected1,
            input2_filename:str,
            # expected2,
    ):
    logger.info(f'running {target_path!s}')
    if not target_path.exists():
        raise FileNotFoundError(f'target path not found: {target_path}')

    logger.info(f'importing {target_path, python_filename}')
    module = load_module(target_path, python_filename)

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