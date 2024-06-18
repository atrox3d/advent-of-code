'''
For example, suppose you have the following replacements:

e => H
e => O
H => HO
H => OH
O => HH

If you'd like to make HOH, you start with e, and then make the following replacements:

e => O to get O
O => HH to get HH
H => OH (on the second H) to get HOH

So, you could make HOH after 3 steps. Santa's favorite molecule, HOHOHO, 
can be made in 6 steps.

'''
from calibrator import indexall, multireplace, calibrate

def build_steps(molecule:str, replacements:list[dict], stop='e') -> tuple[int, list[str]]:
    
    def dict_value_len(a):
        v, *_ = a.values()
        return len(v)

    product = molecule
    print(f'{product = }')
    
    replacements = sorted(replacements, key=dict_value_len, reverse=True)
    steps = []
    count = 0
    done = False
    while not done:
        for rep in replacements:
            for replace, find in rep.items():
                while product.find(find) != -1:
                    count += 1
                    product = product.replace(find, replace, 1)
                    print(f'{find} -> {replace} = {product}')
                    steps.append(product)
                    if replace == stop:
                        done = True
    return count, steps

if __name__ == '__main__':

    replacements = [
        {'e': 'H'},
        {'e': 'O'},
        {'H': 'HO'},
        {'H': 'OH'},
        {'O': 'HH'},
    ]

    from rules import parse_molecule, parse_rules
    from pathlib import Path
    with open(Path(__file__).parent / 'input1.txt') as fp:
        data = fp.read()
    rules = parse_rules(data)
    molecule = parse_molecule(data)

    santa = 'HOHOHO'
    target = 'HOH'
    start = 'e'
    # e => O to get O
    # O => HH to get HH
    # H => OH (on the second H) to get HOH


    count,steps = build_steps(target, replacements)
    print(count)

    count, steps = build_steps(santa, replacements)
    print(count)

    count, steps = build_steps(molecule, rules)
    print(count)
