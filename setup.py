from pathlib import Path
import json
import csv
import logging

logger = logging.getLogger(__name__)

def prepared(subject, *prepared_args, data=None, **prepared_kwargs):
    data = data or [{"input": None, "expected": None}]
    def decorator(fn):
        def wrapper(target_path:Path, filename:str, *args, **kwargs):
            output_path = target_path / filename
            logger.info(f'creating {subject}: {output_path!s}')
            newline = prepared_kwargs.pop('newline', None)
            with open(str(output_path), 'w', newline=newline) as fp:
                args = list(prepared_args) + list(args)
                kwargs = prepared_kwargs | kwargs
                return fn(data, fp, output_path, *args, **kwargs)
        return wrapper
    return decorator

@prepared('json tests')
def create_json_tests(data, fp, output_path, *args, **kwargs):
    json.dump(data, fp)

@prepared('csv tests', newline='')
def create_csv_tests(data, fp, output_path, *args, **kwargs):
    writer = csv.DictWriter(fp, data[0].keys())
    writer.writeheader()
    for row in data:
        logger.debug(f'writing {row=} to {output_path!s}')
        writer.writerow(row)

@prepared('input file')
def create_input(data, fp, output_path, *args, **kwargs):
    pass

@prepared('README')
def create_readme(data, fp, output_path, year:str, day:str, aoc_url='https://adventofcode.com'):
    lines = [
        f'{aoc_url}/{year}/day/{day}',
        f'{aoc_url}/{year}/day/{day}#part2',
    ]
    for line in lines:
        fp.write(f'{line}\n\n')

@prepared('python script', 'solution_template.py')
def create_python_solution(data, fp, output_path, template):
    with open(template) as infp:
        script = infp.read()
        fp.write(script)

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
    create_readme(target_path, readme_filename, year, day, aoc_url)
    create_python_solution(target_path, python_filename)
