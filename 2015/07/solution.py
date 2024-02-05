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

REGEX_LR = r'^(.+)\s->\s(.+$)'
REGEX_EXPR = r'^(\d+|\w+)*\s*(AND|OR|NOT|LSHIFT|RSHIFT)*\s*(\d+|\w+)*'

def split_lr(line: str) -> tuple[tuple]:
    found = re.match(REGEX_LR, line)
    return found.groups()

def parse_expr(expr: str) -> tuple:
    found = re.match(REGEX_EXPR, expr)
    groups = [int(item) if item is not None and item.isnumeric()
              else item
              for item in found.groups()]
    return groups

def build_ports(quiz_input: list[str]) -> dict:
    ports = {}
    for line in quiz_input:
        expr, port = split_lr(line)
        if ports.get(port, False):
            raise ValueError(f'multiple values for port {port}')
        ports[port] = parse_expr(expr)
    return ports

def find_root(port, ports, stack=[]):
    try:
        expr = ports[port]
    except KeyError:
        return stack
    
    if {port:expr} in stack:
        return stack
    
    stack.append({port:expr})

    match expr:
        case lvalue, None, None:
            logger.debug(f'{port} = {lvalue}')
            if isinstance(lvalue, str):
                stack = find_root(lvalue, ports, stack)
        case op, None, rvalue:
            logger.debug(f'{port} = {op} {rvalue}')
            if isinstance(rvalue, str):
                stack = find_root(rvalue, ports, stack)
        case lvalue, op, rvalue:
            logger.debug(f'{port} = {lvalue} {op} {rvalue}')
            if isinstance(lvalue, str):
                stack = find_root(lvalue, ports, stack)
            if isinstance(rvalue, str):
                stack = find_root(rvalue, ports, stack)
        case _:
            raise ValueError(expr)
    return stack

def compute(lvalue, op, rvalue):
    """
    x << y
    Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
    x >> y
    Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
    x & y
    Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
    x | y
    Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
    ~ x
    Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
    x ^ y
    Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.
    """
    match op:
        case 'LSHIFT':
            return lvalue << rvalue
        case 'RSHIFT':
            return lvalue >> rvalue
        case 'OR':
            return lvalue | rvalue
        case 'AND':
            return lvalue & rvalue
        case 'XOR':
            return lvalue ^ rvalue
        case 'NOT':
            return ~ rvalue
        case _:
            raise ValueError(f'unknown operator {op}')

def process(stack: list[dict[tuple]]) -> int:
    vars = {}
    total = 0
    for item in stack:
        for dest, expr in item.items():
            print(f'{dest} = {expr}')
        match expr:
            case lvalue, None, None:
                logger.debug(f'{dest} = {lvalue}')
                vars[dest] = lvalue
                value = lvalue

            case op, None, rvalue:
                logger.debug(f'{dest} = {op} {rvalue}')
                try:
                    rvalue = vars[rvalue]
                except KeyError:
                    pass
                value = compute(None, op, rvalue)
                vars[dest] = value

            case lvalue, op, rvalue:
                logger.debug(f'{dest} = {lvalue} {op} {rvalue}')
                try:
                    rvalue = vars[rvalue]
                except KeyError:
                    pass
                try:
                    lvalue = vars[lvalue]
                except KeyError:
                    pass
                value = compute(lvalue, op, rvalue)
                vars[dest] = value
            case _:
                raise ValueError(expr)
        print(vars)
        try:
            total += value
        except TypeError as te:
            print(repr(te), f'{value = }')
    return total

def solution(quiz_input):
    pass_test = { 'd': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079, 'x': 123, 'y': 456    }
    zero = {k:0 for k in pass_test}

    ports = build_ports(quiz_input)
    stack = find_root('a', ports)
    for item in reversed(stack):
        print(item)
    result = process(reversed(stack))
    return result

if __name__ == '__main__':
    main.main(solution, level='INFO')