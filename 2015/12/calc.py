
def find_numbers(data, skip=None, numbers=None):
    numbers = [] if numbers is None else numbers

    if isinstance(data, int):
        print(f'returning {data}')
        numbers.append(data)
    if isinstance(data, list):
        for element in data:
            find_numbers(element, skip, numbers)
    elif isinstance(data, dict):
        if skip not in data.values():
            for k, v in data.items():
                find_numbers(v, skip, numbers)
    return numbers
