import pytest

def test(solution_file:str):
    print(f'testing {solution_file}')
    pytest.main([solution_file])

