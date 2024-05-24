from pathlib import Path
import json
import csv
import logging

logger = logging.getLogger(__name__)

def create_json_tests(target_path:Path, filename:str):
    data = [{"input": None, "expected": None}]
    
    output_path = target_path / filename
    logger.info(f'creating json tests: {output_path!s}')
    
    with open(str(output_path), 'w') as fp:
        json.dump(data, fp)

def create_csv_tests(target_path:Path, filename:str):
    data = [{"input": 'None', "expected": 'None'}]

    output_path = target_path / filename
    logger.info(f'creating csv tests: {output_path!s}')

    with open(str(output_path), 'w', newline='') as fp:
        writer = csv.DictWriter(fp, data[0].keys())
        writer.writeheader()
        for row in data:
            logger.debug(f'writing {row=} to {output_path!s}')
            writer.writerow(row)

def create_input(target_path:Path, filename:str):

    output_path = target_path / filename
    logger.info(f'creating input file: {output_path!s}')

    (output_path).touch()

def create_readme(target_path:Path, year:str, day:str, filename:str, aoc_url='https://adventofcode.com'):
    
    output_path = target_path / filename
    logger.info(f'creating README: {output_path!s}')
    
    lines = [
        f'{aoc_url}/{year}/day/{day}',
        f'{aoc_url}/{year}/day/{day}#part2',
    ]
    with open(str(output_path), 'w') as fp:
        for line in lines:
            fp.write(f'{line}\n\n')

def create_python_solution(target_path:Path, filename:str):
    
    output_path = target_path / filename
    logger.info(f'creating python script: {output_path!s}')
    
    with open('solution_template.py') as infp:
        script = infp.read()
        with open(str(output_path), 'w') as outfp:
            outfp.write(script)

def setup(
            target_path:Path|str, 
            year:str, 
            day:str,
            json_filename:str,
            csv_filename:str,
            input1_filename:str,
            input2_filename:str,
            readme_filename:str,
            python_filename:str,
            aoc_url:str,
            overwrite:bool=False,
            # confirm:typing.Callable[...,bool]=lambda:input('confirm? ')=='y'
            confirm:bool=False
    ):
    target_path = Path(target_path)
    logger.info(f'setting up {target_path!s}')
    if target_path.exists():
        if not overwrite:
            logger.error('missing -o -y to overwrite')
            raise FileExistsError(f'target path exists: {target_path}')
        else:    
            if not confirm:
                logger.warning('use -y option to confirm overwrite')
                raise FileExistsError(f'target path exists: {target_path}')
            else:
                logger.warning(f'overwriting {target_path}')
    
    logger.info(f'creating dir {target_path!s}')
    target_path.mkdir(parents=True, exist_ok=confirm)

    create_json_tests(target_path, json_filename)
    create_csv_tests(target_path, csv_filename)
    create_input(target_path, input1_filename)
    create_input(target_path, input2_filename)
    create_readme(target_path, year, day, readme_filename, aoc_url)
    create_python_solution(target_path, python_filename)
