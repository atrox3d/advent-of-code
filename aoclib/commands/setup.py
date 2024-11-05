from pathlib import Path


def setup(
        template_path:str, 
        solution_path:str, 
        solution_file:str, 
        inputpath:str
    ):
    print(f'setting up {solution_path}')
    if Path(solution_path).exists():
        print(f'WARNING dir {solution_path} exists')
    Path(solution_path).mkdir(parents=True, exist_ok=True)

    print(f'setting up {solution_file}')
    dest_file = Path(solution_file)
    if dest_file.exists():
        raise FileExistsError(f'file {solution_file} already exists')
    
    src_path = Path(template_path)
    with open(src_path / 'solution.py', 'r') as sp:
        with open(solution_file, 'w') as dp:
            dp.write(sp.read())
    
        
    print(f'setting up {inputpath}')
