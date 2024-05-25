from pathlib import Path
import json
import csv
import logging

logger = logging.getLogger(__name__)

def common_ctxman_adapter(subject, newline=None, data=None):
    '''
        performs the operations in common between all functions
            - creating dummy data
            - logging the operation
            - opening of dest file fp
        
        the function runs inside the with context manager
        
        parameters are intended for the decorator to perform preparation ops
    '''
    data = data or [{"input": None, "expected": None}]
    def decorator(fn):
        '''
        (target_path, filename) is used to create output_path and to open fp
        fn signature injects (data, fp and out_path) before args of each function
        then (data, fp, output_path) is used when calling fn and the remaining args 
        for each function get absorbed by *args or **kwargs
        so that the original:
              create_smtng(target_path, filename, some_params)
        is kept when calling create_smtng but only after creating output_path
        and opening fp, so the definition becomes:
              create_smtng(data, fp, output_path, *args, **kwargs)
        and the is called with:
              create_smtng(data, fp, output_path, any_other_params...)
        '''
        def wrapper(target_path:Path, filename:str, *args, **kwargs):
            # build output path for fn and open
            output_path = target_path / filename
            
            with open(str(output_path), 'w', newline=newline) as fp:
                logger.info(f'creating {subject}: {output_path!s}')
                return fn(data, fp, output_path, *args, **kwargs)
        return wrapper
    return decorator

# effective signature: create_json_tests(target_path, filename)
@common_ctxman_adapter(subject='json tests')
def create_json_tests(data, fp, output_path):
    json.dump(data, fp)

# effective signature: create_csv_tests(target_path, filename)
# newline is used inside with open() for DictWriter
@common_ctxman_adapter(subject='csv tests', newline='')
def create_csv_tests(data, fp, output_path):
    writer = csv.DictWriter(fp, data[0].keys())
    writer.writeheader()
    for row in data:
        logger.debug(f'writing {row=} to {output_path!s}')
        writer.writerow(row)

# effective signature: create_input(target_path, filename)
@common_ctxman_adapter(subject='input file')
def create_input(data, fp, output_path):
    ''' just touches the file '''
    pass

# effective signature: create_readme(target_path, filename, year, day, aoc_url)
@common_ctxman_adapter(subject='README')
def create_readme(data, fp, output_path, year:str, day:str, aoc_url='https://adventofcode.com'):
    lines = [
        f'{aoc_url}/{year}/day/{day}',
        f'{aoc_url}/{year}/day/{day}#part2',
    ]
    for line in lines:
        fp.write(f'{line}\n\n')

# effective signature: create_python_solution(target_path, filename, template)
@common_ctxman_adapter(subject='python script')
def create_python_solution(data, fp, output_path, template, year:str, day:str, aoc_url='https://adventofcode.com'):
    head_comment = '\n'.join([
        f"'''",
        f'{aoc_url}/{year}/day/{day}',
        f'{aoc_url}/{year}/day/{day}#part2',
        f"'''",
        '\n\n'
    ])
    with open(template) as infp:
        template_script = infp.read()
        # print(f'{template_script=!r}')
        fp.write(head_comment+template_script)

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
            template_filename:str,
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
    create_python_solution(target_path, python_filename, template_filename, year, day, aoc_url)
