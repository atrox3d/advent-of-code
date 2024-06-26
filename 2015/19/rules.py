from string import ascii_letters

def parse_rules(textinput:str) -> list[dict]:
    ''' parse the content of input and returns a list of dictionaries
    
        every dict contains the letters and relative replacement
    '''
    rules = []
    for line in textinput.splitlines():
        if '=>' in line:
              search, replace = line.split(' => ')
              rules.append({search:replace})
    return rules

def parse_molecule(textinput:str) -> str:
    ''' parse the content of input and returns the molecule '''
    for line in textinput.splitlines():
        if '=>' in line:
            pass
        elif len(line) and line[0] in ascii_letters:
            molecule = line
    return molecule


if __name__ == '__main__':

    from pathlib import Path
    with open(Path(__file__).parent / 'input1.txt') as fp:
        data = fp.read()
    rules = parse_rules(data)
    molecule = parse_molecule(data)

    print(rules)
    assert len(rules) == 43, 'not 43'
    print(molecule)
