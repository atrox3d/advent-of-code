from pathlib import Path
import json
import csv
import logging

logger = logging.getLogger(__name__)

def common_ctxman_adapter(subject, *prepare_args, data=None, **prepare_kwargs):
    '''
        performs the operations in common between all functions
            - dummy data
            - logging
            - opening of dest file
        
        the function runs inside the with context manager
        
        parameters are intended for the decorator

        any other arg or kwarg is merged into function's args and kwargs
        
        the function may or may not use these parameters
    '''
    # prepare commond vars
    data = data or [{"input": None, "expected": None}]
    newline = prepare_kwargs.pop('newline', None)
    def decorator(fn):
        # wrapper signature differs from fn signature
        def wrapper(target_path:Path, filename:str, *args, **kwargs):
            # build output path for fn
            output_path = target_path / filename
            
            with open(str(output_path), 'w', newline=newline) as fp:
                # merge remaining extra args, kwargs
                args = list(prepare_args) + list(args)
                kwargs = prepare_kwargs | kwargs
                
                logger.info(f'creating {subject}: {output_path!s}')
                # fn signature injects (data, fp and out_path) before 
                # (target_path, filename) that get absorbed by *args or **kwargs
                # togheter with every specific arguments of every function
                # so that the original:
                #       create_smtng(target_path, filename, some_params)
                # is kept when calling create_smtng but the definition becomes:
                #       create_smtng(data, fp, output_path, *args, **kwargs)
                # and the is called with:
                #       create_smtng(data, fp, output_path, target_path, filename, some_params)
                return fn(data, fp, output_path, *args, **kwargs)
        return wrapper
    return decorator

@common_ctxman_adapter(subject='json tests')
# effective signature: create_json_tests(target_path:Path, filename:str)
def create_json_tests(data, fp, output_path):
    json.dump(data, fp)

@common_ctxman_adapter(subject='csv tests', newline='')
# effective signature: create_csv_tests(target_path:Path, filename:str)
# newline is used inside with open()
def create_csv_tests(data, fp, output_path):
    writer = csv.DictWriter(fp, data[0].keys())
    writer.writeheader()
    for row in data:
        logger.debug(f'writing {row=} to {output_path!s}')
        writer.writerow(row)

@common_ctxman_adapter(subject='input file')
# effective signature: create_input(target_path:Path, filename:str)
def create_input(data, fp, output_path):
    ''' just touches the file '''
    pass

@common_ctxman_adapter(subject='README')
# effective signature: create_readme(target_path:Path, filename:str, year, day, aoc_url)
def create_readme(data, fp, output_path, year:str, day:str, aoc_url='https://adventofcode.com'):
    lines = [
        f'{aoc_url}/{year}/day/{day}',
        f'{aoc_url}/{year}/day/{day}#part2',
    ]
    for line in lines:
        fp.write(f'{line}\n\n')

@common_ctxman_adapter(subject='python script')
# effective signature: create_python_solution(target_path:Path, filename:str, template)
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
    create_python_solution(target_path, python_filename, template_filename)
