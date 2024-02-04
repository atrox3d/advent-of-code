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
    logger.debug(f'{line = }')
    found = re.match(REGEX_LR, line)
    return found.groups()

def build_ports(quiz_input: list[str]) -> dict:
    ports = {}
    for line in quiz_input:
        logger.debug(f'{line = }')
        expr, port = split_lr(line)
        logger.debug(f'{expr, port = }')
        if ports.get(port, False):
            raise ValueError(f'multiple values for port {port}')
        ports[port] = parse_expr(expr)
        logger.debug(f'ports[{port}] = {ports[port]}')

    return ports

def build_dependencies(ports: dict[str, tuple[str]]) -> dict:
    dependecies = {}
    for port, expr in ports.items():
        


def parse_expr(expr: str) -> tuple:
    logger.debug(f'{expr = }')
    found = re.match(REGEX_EXPR, expr)
    # filtered
    return found.groups()

def solution(quiz_input):
    pass_test = { 'd': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079, 'x': 123, 'y': 456    }
    zero = {k:0 for k in pass_test}

    ports = build_ports(quiz_input)
    return zero

if __name__ == '__main__':
    main.main(solution, level='DEBUG')