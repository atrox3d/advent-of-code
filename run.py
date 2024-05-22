from pathlib import Path


def run(target_path:Path|str):
    print(f'running {target_path!s}')
    if not target_path.exists():
        raise FileNotFoundError(f'target path not found: {target_path}')