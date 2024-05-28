import argparse
import os
import sys
from pathlib import Path

from atrox3d.logger import logmanager
from atrox3d.logger import modulelogging

from run import run
from setup import setup

def parse(*args):
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

    return parser.parse_args(*args)

def format_day(day) -> str:
    return f'{day:>02}' 

def get_path(base_dir:Path, year:str, day:str) -> Path:
    day = format_day(day)
    target_path = base_dir / year / day
    return target_path

if __name__ == '__main__':
    args = parse('run 2015 15'.split())

    logmanager.setup_logging('DEBUG', logfile='aoc.log')
    modulelogging.set_logger_level_for_modules('INFO', logmanager, modulelogging)
    modulelogging.set_logger_level_for_modules('DEBUG', setup, run)
    logger = logmanager.get_logger(__name__, 'DEBUG')
    logger.info(args)

    CUR_DIR = Path(os.getcwd())
    SCRIPT_DIR = Path(sys.path[0])

    target_path = get_path(SCRIPT_DIR, args.year, args.day)
    logger.info(f'{target_path = }')

    logmanager.setup_logging('DEBUG', logfile=target_path / f'{args.year}{format_day(args.day)}.log', force=True)
    try:
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
    
        if args.command == 'run':
            logger.info('executing run')
            run(
                    target_path=target_path, 
                    python_filename=args.pythonscript or 'main.py',
                    input1_filename=args.input1 or 'input1.txt',
                    # expected1=None,
                    input2_filename=args.input2 or 'input2.txt',
                    # expected2=None,
            )
            logger.info('executed run')
    except FileExistsError as fee:
        logger.error(f'{fee}')
    except FileNotFoundError as fnfe:
        logger.error(f'{fnfe}')
    except AssertionError as ae:
        logger.error(f'{ae}')
    except Exception as e:
        logger.error(f'{e}')
    else:
        logger.info('entering try/else')
        problems = False
        logger.info(f'{args.command} on {target_path} executed succesfully')
        logger.info('quitting')
    finally:
        if problems:
            logger.fatal(f'errors executing {args.command} on {target_path}')
