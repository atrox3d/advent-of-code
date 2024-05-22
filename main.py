import argparse
import os
import sys
from pathlib import Path

def parse():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest='command', help='Commands to run', required=True)

    setup = subparsers.add_parser('setup')
    setup.add_argument('year')
    setup.add_argument('day')

    run = subparsers.add_parser('run')
    run.add_argument('year')
    run.add_argument('day')

    return parser.parse_args()

def get_path(base_dir:Path, year:str, day:str) -> Path:
    day = f'{day:>02}'
    target_path = base_dir / year / day
    return target_path

def setup(target_path:Path|str):
    print(f'setting up {target_path!s}')
    if target_path.exists():
        raise FileExistsError(f'target path exists: {target_path}')

def run(target_path:Path|str):
    print(f'running {target_path!s}')
    if not target_path.exists():
        raise FileNotFoundError(f'target path not found: {target_path}')


if __name__ == '__main__':
    args = parse()
    print(args)

    CUR_DIR = Path(os.getcwd())
    SCRIPT_DIR = Path(sys.path[0])

    target_path = get_path(SCRIPT_DIR, args.year, args.day)

    try:
        problems = True
        if args.command == 'setup':
            setup(target_path)
    
        if args.command == 'run':
            run(target_path)
    except FileExistsError as fee:
        print(f'ERROR | {fee}')
    except FileNotFoundError as fnfe:
        print(f'ERROR | {fnfe}')
    else:
        problems = False
        print(f'{args.command} on {target_path} executed succesfully')
    finally:
        if problems:
            print(f'errors executing {args.command} on {target_path}')
        print('quitting')
