import re


try:
    from auntsue import AuntSue, AuntSue2
except: 
    from. auntsue import AuntSue, AuntSue2

def parse_aunts_to_dict(quiz_input:str) -> dict:
    aunts = {}
    # aunt_pattern = r'^Sue (?P<id>\d+): (?P<properties>.+)'
    # props_pattern = r'(?P<thing>\w+): (?P<qty>\d+)'
    for line in quiz_input.splitlines():
        # result = re.match(aunt_pattern, line)
        # aunt_id, props = result.groupdict().values()
        # aunts[aunt_id] = {}
        # for prop in props.split(', '):
        #     thing, qty = re.match(props_pattern, prop).groupdict().values()
        #     aunts[aunt_id].update({thing:int(qty)})
        aunt = AuntSue.from_string(line)
        aunts[aunt.id] = aunt
    return aunts

def parse_aunts_oop(quiz_input:str, aunt_class) -> dict:
    aunts = {}
    aunt_pattern = r'^Sue (?P<id>\d+): (?P<properties>.+)'
    props_pattern = r'(?P<thing>\w+): (?P<qty>\d+)'
    for line in quiz_input.splitlines():
        result = re.match(aunt_pattern, line)
        aunt_id, props = result.groupdict().values()
        aunt_id = int(aunt_id)
        aunts[aunt_id] = aunt_class(aunt_id)
        for prop in props.split(', '):
            thing, qty = re.match(props_pattern, prop).groupdict().values()
            setattr(aunts[aunt_id], thing, int(qty))
    return aunts

def parse_aunts(quiz_input:str, aunt_class) -> dict:
    return parse_aunts_oop(quiz_input, aunt_class)


def get_tape_dict() -> dict:
    return {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }

def get_tape_oop() -> AuntSue:
    aunt = AuntSue(None)
    for k, v in get_tape_dict().items():
        setattr(aunt, k, v)
    return aunt

def get_tape() -> AuntSue | dict:
    return get_tape_oop()

