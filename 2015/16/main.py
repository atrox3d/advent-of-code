'''
https://adventofcode.com/2015/day/16
https://adventofcode.com/2015/day/16#part2

--- Day 16: Aunt Sue ---
Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a 
few specific compounds in a given sample, 
as well as how many distinct kinds of those compounds there are. 
According to the instructions, these are what the MFCSAM can detect:

children, by human DNA age analysis.
cats. It doesn't differentiate individual breeds.
Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
goldfish. No other kinds of fish.
trees, all in one group.
cars, presumably by exhaust or gasoline or something.
perfumes, which is handy, since many of your Aunts Sue wear a few kinds.
In fact, many of your Aunts Sue have many of these. 
You put the wrapping from the gift into the MFCSAM. 
It beeps inquisitively at you a few times and then prints out a message 
on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?
'''


from pathlib import Path
import logging
import re
logger = logging.getLogger(__name__)

from auntsue import AuntSue

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

def parse_aunts_oop(quiz_input:str) -> dict:
    aunts = {}
    aunt_pattern = r'^Sue (?P<id>\d+): (?P<properties>.+)'
    props_pattern = r'(?P<thing>\w+): (?P<qty>\d+)'
    for line in quiz_input.splitlines():
        result = re.match(aunt_pattern, line)
        aunt_id, props = result.groupdict().values()
        aunts[aunt_id] = AuntSue(aunt_id)
        for prop in props.split(', '):
            thing, qty = re.match(props_pattern, prop).groupdict().values()
            setattr(aunts[aunt_id], thing, int(qty))
    return aunts

def parse_aunts(quiz_input:str) -> dict:
    return parse_aunts_oop(quiz_input)


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

def solution1(quiz_input):
    aunts = parse_aunts(quiz_input)
    tape = get_tape()

    for auntid, aunt in aunts.items():
        print(auntid, aunt)
        for k, v in vars(aunt):
            if v is not None and getattr(tape, k) == v:
                continue
            else:
                break

    

def solution2(quiz_input):
    # print(f'{quiz_input = !r}')
    return None

def load_input(filename):
    with open(filename, 'r') as fp:
        return fp.read()

def main(
            path:Path|str,
            input_file1:str,
            input_file2:str,
    ):
    logger.info('entering module.main')
    for id, (input_file, solution) in enumerate(zip(
            (input_file1, input_file2), 
            (solution1, solution2)
        ), start=1):
        input_path = path / input_file
        logger.info(f'running: file {input_path}')
        input_value = load_input(input_path)
        result = solution(input_value)
        logger.info(f'solution {id}: {result = }')
    logger.info('exiting module.main')

class SolutionNotFoundError(Exception): pass
def test(
            path:Path|str,
            part,
            test_file:str=None,
            expected=None
    ):
    logger.info('entering module.test')
    test_path = path / test_file

    logger.info(f'testing: file {test_path}')
    logger.info(f'testing: {expected = }')
    
    test_value = load_input(test_path)
    try:
        solution_name = f'solution{part}'
        solution = globals()[solution_name]
    except KeyError as ke:
        raise SolutionNotFoundError(f'function {solution_name} not found')
    
    result = solution(test_value, test=True)
    result = str(result)
    assert result == expected, f'TEST FAILED: {result=!r} != {expected!r}'
    logger.info('exiting module.test')

if __name__ == '__main__':
    print('please run root main.py')