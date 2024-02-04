import logging
import sys, os
import re


sys.path.append(os.getcwd())
from aoclib import main

logger = logging.getLogger(__name__)

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


def solution(quiz_input):
    pass_test = { 'd': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079, 'x': 123, 'y': 456    }
    zero = {k:0 for k in pass_test}
    # logger.debug(f'{quiz_input = }')

    port_inits = get_initial_ports(quiz_input)
    ports = get_instructions_by_port(quiz_input)
    # print_first_level_creation(quiz_input, port_inits, ports)
    for port in port_inits:
        for dest, lines in ports.items():
            if port == dest:
                logger.info(f'{dest = }')
                logger.info(f'{port = }')
                for line in lines:
                    logger.info(f'CALL get_call_stack | {port =}, {line =}')
                    get_call_stack(port, ports, [line])
        print()

    return zero

def get_call_stack(port, ports, stack=[]):
    tabs = ' ' * (len(stack)+1)
    tabs = ''
    logger.debug(f'{tabs}ENTER')
    for dest, lines in ports.items():
        for line in lines:
            if port in line and port != dest and line not in stack:
                for pos, needle in enumerate(stack[:10]):
                    logger.debug(f'{tabs}stack[{pos}] = {needle}')
                if len(stack) > 10:
                    logger.debug(f'{tabs}stack[x] = ...')
                stack.append(line)
                logger.debug(f'{tabs}{port =}, {dest = }, {line =}')
                statement = line[:-2]
                match [item for item in statement if item is not None]:
                    case left, op, right:
                        logger.info(f'{tabs}{left = }, {op = }, {right =}')
                        if isinstance(left, str):
                            get_call_stack(left, ports, stack)
                        if isinstance(right, str):
                            get_call_stack(right, ports, stack)
                    case op, right:
                        logger.info(f'{tabs}{op = }, {right =}')
                        if isinstance(right, str):
                            get_call_stack(right, ports, stack)
                        pass
                    case _:
                        raise ValueError(f'{statement = }')
                get_call_stack(dest, ports, stack)
    logger.debug(f'{tabs}RETURN')


def print_first_level_creation(quiz_input, port_inits, ports):
    for initport in port_inits:
        for port, lines in ports.items():
            for line in lines:
                if initport in line[:-2:]:
                    print(port, line)
    
def get_initial_ports(quiz_input):
    port_inits = {}
    assign = re.compile(r'^(\d+) (->) (\w+)$')
    for line in quiz_input:
        found = assign.match(line)
        if found is not None:
            port = found.groups()[-1]
            port_inits[port] = found[1]
    return port_inits

def get_instructions_by_port(quiz_input):
    from collections import defaultdict
    ports = defaultdict(list)
    for line in quiz_input:
        groups = regex_tester(line, REGEX2)
        groups = [int(item) if item and item.isnumeric() else item for item in groups]
        port = groups[-1]
        ports[port].append(groups)
    return ports

def regex_tester(line, regex):
    tokens = re.compile(regex)
    logger.debug(f'{line = }')
    found = tokens.match(line)
    logger.debug(f'{found = }')

    if found:
        groups = found.groups()
        logger.debug(f'{groups = }')
        # groupd = found.groupdict()
        # logger.debug(f'{groupd = }')
        trim = [val for val in groups if val]
        logger.debug(f'{trim = }')
        logger.debug(f'enumerate: {list(enumerate(groups))}')
        logger.debug('')
        return groups
    else:
        logger.error(f'not found: {line}')
        exit()


if __name__ == '__main__':
    main.main(solution, level='INFO')