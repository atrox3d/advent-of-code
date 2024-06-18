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
product: str = santa[:]
# e => O to get O
# O => HH to get HH
# H => OH (on the second H) to get HOH
def xxx(a):
    v, *_ = a.values()
    return len(v)

# print(sorted(rules, key=xxx, reverse=True))
replacements = sorted(replacements, key=xxx, reverse=True)
steps = []
print(product)
for rep in replacements:
    for replace, find in rep.items():
        while product.find(find) != -1:
            product = product.replace(find, replace, 1)
            print(find, replace, product)
            steps.append(product)
print(len(steps))