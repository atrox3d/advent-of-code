import types


def run(module:types.ModuleType, input_file:str):
    print(f'running {module.__file__}::solution({input_file})')
    module.solution(input_file)
