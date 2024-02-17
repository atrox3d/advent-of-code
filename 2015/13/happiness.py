
def setup_table(quiz_input: list[str]) -> dict[dict]:
    table = {}
    for line in quiz_input:
        match line.split():
            case name, 'would', op, qty, what, 'units', 'by', 'sitting', 'next', 'to', whom:
                op = -1 if op == 'lose' else 1
                qty = int(qty) * op
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

if __name__ == '__main__':
    input_text = '''A would gain 54 happiness units by sitting next to B.
A would lose 79 happiness units by sitting next to C.
A would lose 2 happiness units by sitting next to D.
B would gain 83 happiness units by sitting next to A.
B would lose 7 happiness units by sitting next to C.
B would lose 63 happiness units by sitting next to D.
C would lose 62 happiness units by sitting next to A.
C would gain 60 happiness units by sitting next to B.
C would gain 55 happiness units by sitting next to D.
D would gain 46 happiness units by sitting next to A.
D would lose 7 happiness units by sitting next to B.
D would gain 41 happiness units by sitting next to C.'''
    lines = input_text.split('\n')
    for line in lines:
        print(line)
    
    print(setup_table(lines))