from pathlib import Path
import json
import csv
import logging
import importlib.util

logger = logging.getLogger(__name__)

def run(
            target_path:Path|str, 
            year:str, 
            day:str,
            json_filename:str,
            csv_filename:str,
            input1_filename:str,
            input2_filename:str,
            readme_filename:str,
            python_filename:str,
            aoc_url:str
    ):
    print(f'running {target_path!s}')
    if not target_path.exists():
        raise FileNotFoundError(f'target path not found: {target_path}')

    file_path = target_path / python_filename
    module_name = file_path.stem

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Verify contents of the module:
    print(dir(module))
    print('running main')
    module.main()
    print('runned main')