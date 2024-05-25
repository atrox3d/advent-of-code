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

    return parser.parse_args(*args)

def get_path(base_dir:Path, year:str, day:str) -> Path:
    day = f'{day:>02}'
    target_path = base_dir / year / day
    return target_path

if __name__ == '__main__':
    args = parse()

    logmanager.setup_logging('DEBUG')
    modulelogging.set_logger_level_for_modules('INFO', logmanager, modulelogging)
    modulelogging.set_logger_level_for_modules('DEBUG', setup, run)
    logger = logmanager.get_logger(__name__, 'DEBUG')
    logger.info(args)

    CUR_DIR = Path(os.getcwd())
    SCRIPT_DIR = Path(sys.path[0])

    target_path = get_path(SCRIPT_DIR, args.year, args.day)
    logger.info(f'{target_path = }')

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
            run(
                    target_path=target_path, 
                    expected1=None,
                    expected2=None,
                    input1_filename='input1.txt',
                    input2_filename='input2.txt',
                    python_filename='main.py',
            )
    except FileExistsError as fee:
        logger.error(f'{fee}')
    except FileNotFoundError as fnfe:
        logger.error(f'{fnfe}')
    except AssertionError as ae:
        logger.error(f'{ae}')
    else:
        problems = False
        logger.info(f'{args.command} on {target_path} executed succesfully')
        logger.info('quitting')
    finally:
        if problems:
            logger.fatal(f'errors executing {args.command} on {target_path}')
