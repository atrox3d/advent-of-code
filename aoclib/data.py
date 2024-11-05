from pathlib import Path
import types

def get_inputfile(
        year:str,
        day:str,
        part:str,
        suffix='txt'
) -> str:
    return f'{year}/{day}/input{part}.{suffix}'

def get_solutionpath(year:str, day:str) -> str:
    solution_path = f'{year}/{day}'
    return solution_path

def get_solutionfile(year:str, day:str, part:str) -> str:
    solution_path = f'{get_solutionpath(year, day)}/part{part}.py'
    return solution_path

def get_solutionpackage(year:str, day:str, part:str) -> str:
    solution_package = f'{year}.{day}.part{part}'
    return solution_package

