import argparse
import os
import sys
from pathlib import Path

import importlib.util
import types

from atrox3d.logger import logmanager
from atrox3d.logger import modulelogging

from run import run
from setup import setup
from test import test

def parse(*args):
    '''parse command line arguments'''

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest='command', help='Commands to run', required=True)

    setup = subparsers.add_parser('setup')
    setup.add_argument('year')
    setup.add_argument('day')
    setup.add_argument('-o', '--overwrite', action='store_true', default=False)
    setup.add_argument('-y', '--confirm', action='store_true', default=False)

    run = subparsers.add_parser('run')
    run.add_argument('year')
    run.add_argument('day')
    run.add_argument('-p', '--pythonscript')
    run.add_argument('-i1', '--input1')
    run.add_argument('-i2', '--input2')

    run = subparsers.add_parser('test')
    run.add_argument('year')
    run.add_argument('day')
    run.add_argument('-p', '--pythonscript')
    run.add_argument('-t', '--testfile')
    run.add_argument('-e', '--expected', required=True)

    return parser.parse_args(*args)

def format_day(day) -> str:
    '''left zero pads day if one digit'''
    return f'{day:>02}' 

def build_target_path(base_dir:Path, year:str, day:str) -> Path:
    '''return path of aoc year/day exercise'''
    day = format_day(day)
    target_path = base_dir / year / day
    return target_path

def load_module(target_path:Path, python_filename:str) -> types.ModuleType:
    '''dynamically loads a module from path and filename'''

    file_path = target_path / python_filename
    module_name = file_path.stem

    logger.debug(f'loading module file: {file_path}')
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    logger.debug(f'creating module fromo spec: {spec}')
    module = importlib.util.module_from_spec(spec)
    logger.debug(f'executing module: {module}')
    spec.loader.exec_module(module)
    return module

if __name__ == '__main__':
    # initialize logging
    logmanager.setup_logging('DEBUG', logfile='aoc.log')
    # set logger level to info for library modules
    modulelogging.set_logger_level_for_modules('INFO', logmanager, modulelogging)
    # set logger level to debug for this script modules
    modulelogging.set_logger_level_for_modules('DEBUG', setup, run)
    # get this module logger
    logger = logmanager.get_logger(__name__, 'DEBUG')

    # args = parse('run 2015 15'.split())
    args = parse()
    logger.info(args)

    CUR_DIR = Path(os.getcwd())
    SCRIPT_DIR = Path(sys.path[0])

    target_path = build_target_path(SCRIPT_DIR, args.year, args.day)
    logger.info(f'{target_path = }')
    try:
        # flag to check if everything ok inside try/finally
        problems = True

        logger.debug(f'{args.command = }')
        if args.command == 'setup':
            setup(
                    target_path=target_path, 
                    year=args.year, 
                    day=args.day,
                    json_filename='tests.json',
                    csv_filename='tests.csv',
                    input1_filename='input1.txt',
                    input2_filename='input2.txt',
                    readme_filename='README.md',
                    python_filename='main.py',
                    template_filename='main_template.py',
                    aoc_url='https://adventofcode.com',
                    overwrite=args.overwrite,
                    confirm=args.confirm
            )
    
        elif args.command in ['run', 'test']:

            # load python solution script
            python_filename = args.pythonscript or 'main.py'
            logger.info(f'importing {target_path, python_filename}')
            module = load_module(target_path, python_filename)
            
            # add separate logfile for imported module
            loggers = modulelogging.get_module_loggers(module)
            logfile = target_path / f'{args.year}{format_day(args.day)}.log'
            for _logger in loggers:
                logmanager.add_logfile(_logger, logfile)
                logmanager.add_stream(_logger)
                # TODO: add format
                _logger.propagate = False
            
            if args.command == 'run':
                logger.info('executing run.run with loaded module')
                run(
                        module,
                        target_path=target_path,
                        input1_filename=args.input1 or 'input1.txt',
                        input2_filename=args.input2 or 'input2.txt',
                )
                logger.info('executed run.run')
            else:
                logger.info('executing test.test with loaded module')
                test(
                        module,
                        target_path=target_path,
                        test_filename=args.testfile or 'test.txt',
                        expected=args.expected
                )
                logger.info('executed test.test')
            
        else:
            raise NotImplementedError(f'command {args.command}')
        
    except FileExistsError as fee:
        logger.error(f'{fee}')
    except FileNotFoundError as fnfe:
        logger.error(f'{fnfe}')
    except AssertionError as ae:
        logger.error(f'{ae}')
    except Exception as e:
        logger.error(f'unexpected exception: {e}')
        logger.exception(e)
    else:
        # logger.info('entering try/else')
        problems = False
        logger.info(f'{args.command} on {target_path} executed succesfully')
        logger.info('quitting')
    finally:
        if problems:
            logger.fatal(f'errors executing {args.command} on {target_path}')
        logger.info('')
