def solution(input_path):
    with open(input_path) as fp:
        input_text = fp.read()
    
    up = input_text.count('(')
    down = input_text.count(')')

    print(f'{up, down = }')
    print(f'{up - down = }')
    return up - down

def test_solution_2015_01_1():
    pass