
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

    def totals1(table, combos):
        totals = []
        ops = []
        for combo in combos:
            prev = ''
            total = 0
            subops = []
            for place in combo + [combo[0]]:
                if prev:
                    subtotal = table[prev][place]+table[place][prev]
                    # subops.append(f'{prev}{place}+{place}{prev}={subtotal}')
                    # subops.append(f'{table[prev][place]}+{table[place][prev]}={subtotal}')
                    total += subtotal
                prev = place
            # ops.append(subops)
            totals.append(total)
        # print(ops)
        print(totals)
        print(max(totals))
    
    def totals2(table, combos):
        totals = []
        ops = []
        for combo in combos:
            total = 0
            subops = []
            for prev, next in zip(combo, combo[1:]+combo[0:1]):
                subtotal = table[prev][next]+table[next][prev]
                # subops.append(f'{prev}{next}+{next}{prev}={subtotal}')
                # subops.append(f'{table[prev][next]}+{table[next][prev]}={subtotal}')
                total += subtotal
            # ops.append(subops)
            totals.append(total)
        # print(ops)
        print(totals)
        print(max(totals))
    
    totals1(table, combos)
    totals2(table, combos)