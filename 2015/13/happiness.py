
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

    combos = [item for item in rpermute([place for place in table]) if item[0]=='A']
    print(combos)

    
    def totals2(table, combos):
        totals = []
        for combo in combos:
            total = 0
            for prev, next in zip(combo, combo[1:]+combo[0:1]):
                subtotal = table[prev][next]+table[next][prev]
                total += subtotal
            totals.append(total)
        print(totals)
        print(max(totals))
    
    totals2(table, combos)