from pathlib import Path


def setup(solution_path:str, solution_file:str, inputpath:str):
    print(f'setting up {solution_path}')
    if Path(solution_path).exists():
        raise FileExistsError(f'dir {solution_path} already exists')
    print(f'setting up {solution_file}')
    print(f'setting up {inputpath}')
