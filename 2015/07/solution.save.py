"""
--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires 
and bitwise logic gates! Unfortunately, little Bobby is a little 
under the recommended age range, and he needs help assembling 
the circuit.

Each wire has an identifier (some lowercase letters) and can 
carry a 16-bit signal (a number from 0 to 65535). A signal is 
provided to each wire by a gate, another wire, or some specific 
value. Each wire can only get a signal from one source, 
but can provide its signal to multiple destinations. 
A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect 
the parts together: 
x AND y -> z means to connect wires x and y to an AND gate, 
and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y 
is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is 
left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value 
from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT 
(right-shift). 

If, for some reason, you'd like to emulate the circuit instead, 
almost all programming languages (for example, C, JavaScript, 
or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet 
(provided as your puzzle input), what signal is ultimately 
provided to wire a?
"""
import logging
import sys, os
import re, json
from pathlib import Path

sys.path.append(os.getcwd())
from aoclib import main

logger = logging.getLogger(__name__)

REGEX1 = (
        r'^(?P<left>'           # 0
        r'(\w+)|'               # 1 2
        r'(\d+)|'               # 3 4
        r'(\w+) (\w+) (\w+)|'   # 5 6
        r'(\w+) (\w+)'          # 6 7
        r')'
        r' (->) '               # 8
        r'(?P<right>\w+)$'      # 9
)

REGEX2 = (
        r'^(\d+|\w+)*\s*'
        r'(AND|OR|NOT|LSHIFT|RSHIFT)*\s*(\d+|\w+)*'
        r' (->) '
        r'(\w+)$'
)

def split_lr(line: str) -> tuple[tuple]:
    '''
    returns a tuple containing (left, right) parts of the expression
    separated by ' -> '
    '''
    REGEX_LR = r'^(.+)\s->\s(.+$)'
    found = re.match(REGEX_LR, line)
    return found.groups()

def parse_gate(expr: str) -> tuple:
    '''
    returns a tuple containing possible lvalue, operator and rvalue
    tries to convert numeric values to integers, eg. a=10
    '''
    REGEX_EXPR = r'^(\d+|\w+)*\s*(AND|OR|NOT|LSHIFT|RSHIFT)*\s*(\d+|\w+)*'
    found = re.match(REGEX_EXPR, expr)
    groups = [int(item) if item is not None and item.isnumeric()
              else item
              for item in found.groups()]
    return groups

def build_wires(quiz_input: list[str]) -> dict:
    '''
    builds a dictionary with key = portname and value = expression tuple
    '''
    wires = {}
    for line in quiz_input:
        gate, wid = split_lr(line)
        if wires.get(wid, False):
            raise ValueError(f'multiple values for wire {wid}')
        wires[wid] = parse_gate(gate)
    return wires

def wire2str(wire: dict[str, tuple]) -> str:
    '''
    prints the human format: p = a op b
    '''
    wid, gate = wire
    match gate:
        case lvalue, None, None:
            return f'{wid} = {lvalue}'
        case op, None, rvalue:
            return f'{wid} = {op} {rvalue}'
        case lvalue, op, rvalue:
            return f'{wid} = {lvalue} {op} {rvalue}'
        case _:
            raise ValueError(gate)

def get_wire_value(wid:str, wires: dict[str, tuple]) -> int:
    if isinstance(wid, int):
        logger.debug(f'{wid = } is int, returning')
        return wid
    
    gate = wires[wid]
    if isinstance(gate, int):
        logger.debug(f'{wid=} {gate = } is int, returning')
        return gate
    # logger.debug(f'{gate = }')
    
    match gate:
        case lvalue, None, None:
            logger.debug(f'match: {wid} = {lvalue}')
            value = get_wire_value(lvalue, wires)
        
        case op, None, rvalue,:
            logger.debug(f'match: {wid} = {op} {rvalue}')
            match op:
                case 'NOT':
                    value = ~get_wire_value(rvalue, wires)
        
        case lvalue, op, rvalue:
            logger.debug(f'match: {wid} = {lvalue} {op} {rvalue}')
            match op:
                case 'AND':
                    value = get_wire_value(lvalue, wires) & get_wire_value(rvalue, wires)
                case 'OR':
                    value = get_wire_value(lvalue, wires) | get_wire_value(rvalue, wires)
                case 'LSHIFT':
                    value = get_wire_value(lvalue, wires) << get_wire_value(rvalue, wires)
                case 'RSHIFT':
                    value = get_wire_value(lvalue, wires) >> get_wire_value(rvalue, wires)
        case _:
            raise ValueError(f'{gate}')
    
    if isinstance(value, int):
        logger.debug(f'updating wires[{wid}] = {value}')
        wires[wid] = value
    return value

def solution(quiz_input):
    '''
    '''
    pass_test = { 'd': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079, 'x': 123, 'y': 456    }
    zero = {k:0 for k in pass_test}
    wires = build_wires(quiz_input)
    # stack = find_root('a', ports)
    # stack = list(reversed(stack))
    # for item in stack:
        # repr_stack_item(item, logger.info)
    # logger.info(f'{len(quiz_input), len(stack ) = }')
    # result = process(stack)
    # return result
    for wire in wires.items():
        print(wire2str(wire))
    
    value = get_wire_value('a', wires)
    print(value)
    
if __name__ == '__main__':
    handlers = [
        logging.FileHandler(
            str(Path(sys.argv[0]).parent / Path(__file__).stem) + '.log',
            mode='w'
            ),
        logging.StreamHandler()
    ]
    main.main(solution, level='DEBUG', handlers=handlers)