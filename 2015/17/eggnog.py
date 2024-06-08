import itertools

example = 25, [20, 15, 10, 5, 5]
target, numbers = example

def subset_sum(numbers: list, target: int) -> list[list]:
    combos = []
    for i in range(len(numbers)):
        for combo in itertools.combinations(numbers, i):
            if sum(combo) == target:
                combos.append(combo)
    return combos

def test_combinations(data, max_len=None):
    for r in range(max_len if max_len is not None else len(data)):
        print(f'{r=}')
        for combo in itertools.combinations(data, r=r):
            print(combo)
        print()

print(subset_sum(numbers, target))