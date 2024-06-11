'''
For example, imagine a simpler machine that supports only the following replacements:

H => HO
H => OH
O => HH
Given the replacements above and starting with HOH, 
the following molecules could be generated:

HOH 

HOOH (via H => HO on the first H).
HOHO (via H => HO on the second H).
OHOH (via H => OH on the first H).
HOOH (via H => OH on the second H).
HHHH (via O => HH).

So, in the example above, there are 4 distinct molecules (not five, because HOOH appears 
twice) after one replacement from HOH. 

Santa's favorite molecule, HOHOHO, can become 7 distinct molecules 
(over nine replacements: six from H, and three from O).

The machine replaces without regard for the surrounding characters. 
For example, given the string H2O, the transition H => OO would result in OO2O.

'''

def calibrate(medicine, replacements):
    molecules = set()
    for i, char in enumerate(medicine):
            pre = medicine[:i]
            post = medicine[i+1:]
            for replacement in replacements:
                for search, replace in replacement.items():
                    if char == search:
                            molecule = pre + replace + post
                            molecules.add(molecule)
    return molecules

def parse_rules(textinput:str) -> tuple[list, str]:
    from string import ascii_letters
    rules = []
    for line in textinput.splitlines():
        if '=>' in line:
              search, replace = line.split(' => ')
              rules.append({search:replace})
        elif len(line) and line[0] in ascii_letters:
            molecules = line
            
    return rules, molecules

if __name__ == '__main__':
    replacements = [
        {'H': 'HO'},
        {'H': 'OH'},
        {'O': 'HH'},
    ]

    santas = 'HOHOHO'
    medicine = 'HOH'

    print(calibrate(medicine, replacements))
    print(calibrate(santas, replacements))

    replacements = [
        {'H': 'OO'},
    ]

    print(calibrate('H20', replacements))

    from pathlib import Path
    with open(Path(__file__).parent / 'input1.txt') as fp:
        rules, molecules = parse_rules(fp.read())
    print(rules)
    assert len(rules) == 43, 'not 43'
    print(molecules)
