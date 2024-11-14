

def get_happiness(quiz_input: list[str]) -> dict[dict]:
    happiness = {}
    for line in quiz_input:
        match line.split():
            case name, 'would', op, qty, what, 'units', 'by', 'sitting', 'next', 'to', whom:
                op = -1 if op == 'lose' else 1
                qty = int(qty) * op
                whom = whom[:-1]
                happiness[name] = happiness.get(name, {})
                happiness[name].update({whom:qty})
            case _:
                raise ValueError()
    return happiness


def totals(table, combos):
    totals = []
    for combo in combos:
        total = 0
        for prev, next in zip(combo, combo[1:]+combo[0:1]):
            subtotal = table[prev][next]+table[next][prev]
            total += subtotal
        totals.append(total)
    return totals

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
    
    happiness = get_happiness(lines)
    print(json.dumps(happiness, indent=4))

    names = [name for name in happiness]
    permutations = rpermute(names)
    combos = [item for item in permutations if item[0]==names[0]]
    print(combos)

    print(max(totals(happiness, combos)))
