from pathlib import Path
import json
import csv
import logging

logger = logging.getLogger(__name__)

def create_json_tests(target_path:Path, filename='tests.json'):
    data = [{"input": None, "expected": None}]
    output_path = target_path / filename
    logger.info(f'creating json tests: {output_path!s}')
    with open(str(output_path), 'w') as fp:
        json.dump(data, fp)

def create_csv_tests(target_path:Path, filename='tests.csv'):
    data = [{"input": None, "expected": None}]
    output_path = target_path / filename
    logger.info(f'creating csv tests: {output_path!s}')
    with open(str(output_path), 'w') as fp:
        writer = csv.DictWriter(fp, data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def create_input(target_path:Path, filename:str):
    output_path = target_path / filename
    logger.info(f'creating input file: {output_path!s}')
    (output_path).touch()

def create_readme(target_path:Path, filename='README.md'):
    output_path = target_path / filename
    logger.info(f'creating README: {output_path!s}')
    with open(str(output_path), 'w') as fp:
        fp.write('''https://adventofcode.com/YEAR/day/DAY\nhttps://adventofcode.com/YEAR/day/DAY#part2''')
    
def setup(target_path:Path|str):
    target_path = Path(target_path)
    logger.info(f'setting up {target_path!s}')
    if target_path.exists():
        raise FileExistsError(f'target path exists: {target_path}')
    
    logger.info(f'creating dir {target_path!s}')
    target_path.mkdir(parents=True)

    create_json_tests(target_path)
    create_csv_tests(target_path)
    create_input(target_path, 'input1.txt')
    create_input(target_path, 'input2.txt')
    create_readme(target_path)
