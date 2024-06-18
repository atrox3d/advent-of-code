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
import re

def indexall(find:str, where:str) -> list[int]:
    ''' returns a list of index of every match as opposed to str.index '''

    return [m.start() for m in re.finditer(find, where)]

def multireplace(find:str, replace:str, where:str) -> list[str]:
    ''' replace every occurence of find in str with replace '''
    
    replaced = []
    for index in indexall(find, where):
        pre = where[:index]
        # treat each occurency as a new string
        post = where[index:]
        # reassemble original string and adds to the list
        new = post.replace(find, replace, 1)
        replaced.append(pre+new)
    return replaced


def calibrate(sequence:str, replacements:list[dict[str, str]]) -> set[str]:
    ''' process all occurrencies and add each result without duplicates '''
    
    molecules = set()
    for replacement in replacements:
        for search, replace in replacement.items():
            replaced = multireplace(search, replace, sequence)
            molecules.update(replaced)
    return molecules

if __name__ == '__main__':
    replacements = [
        {'H': 'HO'},
        {'H': 'OH'},
        {'O': 'HH'},
    ]

    santas = 'HOHOHO'
    medicine = 'HOH'

    # for target in (medicine, santas):
    #     done = set()
    #     for rep in replacements:
    #         for find, replace in rep.items():
    #             repls = multireplace(find, replace, target)
    #             print(find, repls)
    #             done.update(repls)
    #     print(done, len(done))
    
    print(calibrate(santas, replacements))
    print(calibrate(medicine, replacements))
    
