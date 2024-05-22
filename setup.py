from pathlib import Path
import json

def create_json_tests(target_path:Path, filename='tests.json'):
    data = [{"input": None, "expected": None}]
    with open(str(target_path / filename), 'w') as fp:
        json.dump(fp, data)


def setup(target_path:Path|str):
    target_path = Path(target_path)
    print(f'setting up {target_path!s}')
    if target_path.exists():
        raise FileExistsError(f'target path exists: {target_path}')