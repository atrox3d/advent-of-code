from pathlib import Path

def copy(src, dest, **subst):
    with open(src, 'r') as sp:
        with open(dest, 'w') as dp:
            content = sp.read()
            for target, replace in subst.items():
                content = content.replace(target, str(replace))
            dp.write(content)

def setup(
        year:str,
        day:str,
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
    src_file = Path(template_path) / 'solution.py'
    copy(src_file, dest_file)

    readme = Path(solution_path) / 'README.md'
    print(f'setting up {readme}')
    if readme.exists():
        print(f'WARNING dir {readme} exists')
    src_file = Path(template_path) / 'README.md'
    copy(src_file, readme, YEAR=year, DAY=day)

    print(f'setting up {inputpath}')
    Path(inputpath).touch()
