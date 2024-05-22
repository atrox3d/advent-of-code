from pathlib import Path
import json
import csv
import logging

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
            aoc_url:str
    ):
    print(f'running {target_path!s}')
    if not target_path.exists():
        raise FileNotFoundError(f'target path not found: {target_path}')