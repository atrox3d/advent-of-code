from pathlib import Path


def setup(target_path:Path|str):
    print(f'setting up {target_path!s}')
    if target_path.exists():
        raise FileExistsError(f'target path exists: {target_path}')