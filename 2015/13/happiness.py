
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

def rpermute(items):
    if len(items) == 1:
        return [items]
    
    out = []
    for item in items:
        for res in rpermute([c for c in items if c!=item]):
            ret = [item,  *res]
            out.append(ret)
    return out

if __name__ == '__main__':
    import json
    from test_data import input_text

    lines = input_text.split('\n')
    for line in lines:
        print(line)
    
    table = setup_table(lines)
    print(json.dumps(table, indent=4))

    # find_max_happiness(table)
    # recurse(table)
    combos = [item for item in rpermute([place for place in table]) if item[0]=='A']
    print(combos)

    totals = []
    for combo in combos:
        prev = ''
        first = ''
        total = 0
        for place in combo:
            if prev:
                total += table[place][prev]+table[prev][place]
            else:
                first = place
            prev = place
        last = place
        total += table[last][first]+table[first][last]
        totals.append(total)
    print(max(totals))