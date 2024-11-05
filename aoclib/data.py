from pathlib import Path
import types

def get_inputpath(
        module:types.ModuleType,
        inputpath:str=None,
        suffix='txt'
) -> str:
    if inputpath is None:
        inputpath = Path(module.__file__).with_suffix(f'.{suffix}')
    return str(inputpath)

def get_solutionpath(year:str, day:str) -> str:
    solution_path = f'{year}/{day}'
    return solution_path

def get_solutionfile(year:str, day:str, part:str) -> str:
    solution_path = f'{get_solutionpath(year, day)}/part{part}.py'
    return solution_path

def get_solutionpackage(year:str, day:str, part:str) -> str:
    solution_package = f'{year}.{day}.part{part}'
    return solution_package

