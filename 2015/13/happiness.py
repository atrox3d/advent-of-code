
def setup_table(quiz_input: list[str]) -> dict[dict]:
    table = {}
    for line in quiz_input:
        match line.split():
            case name, 'would', op, qty, what, 'units', 'by', 'sitting', 'next', 'to', whom:
                op = -1 if op == 'lose' else 1
                qty = int(qty) * op
                whom = whom[:-1]
                table[name] = table.get(name, {})
                table[name].update({whom:qty})
            case _:
                raise ValueError()
    return table


def find_max_happiness(table: dict):
    for name in table:
        print(f'{name = }')
        for near, happiness in table[name].items():
            print(f'{near, happiness=}')

def recurse(table, target=None):
    print(f'{table, target = }')
    if isinstance(table, int):
        print(f'return {table}')
        return table
    
    if target is None:
        values = []
        for target in table:
            print(f'{target = }') # A B C D
            values.append(recurse(table[target], target))
        print(values)
    else:
        print(f'{target = }, {table = }')
        values = []
        for target in table:
            print(target)
            values.append(recurse(table[target], target))
            print()
        return values

if __name__ == '__main__':
    import json
    from test_data import input_text
    from permutations import rpermute

    lines = input_text.split('\n')
    for line in lines:
        print(line)
    
    table = setup_table(lines)
    print(json.dumps(table, indent=4))

    # find_max_happiness(table)
    # recurse(table)
    print(rpermute([place for place in table]))