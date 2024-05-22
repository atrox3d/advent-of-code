from pathlib import Path
import json
import csv

def create_json_tests(target_path:Path, filename='tests.json'):
    data = [{"input": None, "expected": None}]
    with open(str(target_path / filename), 'w') as fp:
        json.dump(fp, data)

def create_csv_tests(target_path:Path, filename='tests.csv'):
    data = [{"input": None, "expected": None}]
    with open(str(target_path / filename), 'w') as fp:
        writer = csv.DictWriter(fp, data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def create_input(target_path:Path, filename:str):
    (target_path / filename).touch()

def create_readme(target_path:Path, filename='README.md'):
    with open(str(target_path / filename), 'w') as fp:
        fp.write('''https://adventofcode.com/YEAR/day/DAY\nhttps://adventofcode.com/YEAR/day/DAY#part2''')
    
def setup(target_path:Path|str):
    target_path = Path(target_path)
    print(f'setting up {target_path!s}')
    if target_path.exists():
        raise FileExistsError(f'target path exists: {target_path}')
    target_path.mkdir()
    create_json_tests(target_path)
    create_csv_tests(target_path)
    create_input(target_path, 'input1.txt')
    create_input(target_path, 'input2.txt')
    create_readme(target_path)
