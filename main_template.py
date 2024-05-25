def solution1(quiz_input):
    print(f'{quiz_input = !r}')
    return None

def solution2(quiz_input):
    print(f'{quiz_input = !r}')
    return None

def load_input(filename):
    with open(filename, 'r') as fp:
        return fp.read()

def main(path, input_file1, expected1, input_file2, expected2):
    for input_file, expected, solution in zip(
            (input_file1, input_file2), 
            (expected1, expected2),
            (solution1, solution2)
        ):
        input_path = path / input_file
        input_value = load_input(input_path)
        result = solution1(input_value)
        assert result == expected, f'{result=} != {expected}'
