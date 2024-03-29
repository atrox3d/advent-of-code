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
import pathlib, sys, os, logging
sys.path.append(os.getcwd())

from aoclib import main

logger = logging.getLogger(__name__)
DIR = pathlib.Path(__file__).parent.absolute()


def solution(quiz_input):

    class Wire:
        items = {}

        def __init__(self, expression, dest_port):
            self.dest_port = dest_port                  # save dest_port
            self.expression = expression                # save expression: ...
            Wire.items[dest_port] = self                # save instance in class dict
            self.value = None                           # no value for now

        def calc(self):
            if self.value is not None:
                logger.debug(f'self.value is not None: {self.value = }')
                return self.value
            else:
                logger.debug(f'match {self.dest_port, self.expression = }')
                match self.expression:
                    case lvalue, op, rvalue:
                        logger.debug(f'{lvalue, op, rvalue =}')
                        match op:
                            case 'AND':
                                self.value = get_port_value(lvalue) & get_port_value(rvalue)
                            case 'OR':
                                self.value = get_port_value(lvalue) | get_port_value(rvalue)
                            case 'LSHIFT':
                                self.value = get_port_value(lvalue) << get_port_value(rvalue)
                            case 'RSHIFT':
                                self.value = get_port_value(lvalue) >> get_port_value(rvalue)
                    case op, rvalue,:
                        logger.debug(f'{op, rvalue=}')
                        match op:
                            case 'NOT':
                                self.value = ~get_port_value(rvalue)
                    case lvalue,:
                        logger.debug(f'assign: {lvalue=}')
                        self.value = get_port_value(lvalue)
                    case _:
                        raise ValueError(f'{self.expression}')
            return self.value
    
    def get_port_value(key):
        try:
            value = int(key)
            logger.debug(f'found {value = }')
            return value
        except:
            logger.debug(f'NOT found value for {key = }')
            # logger.debug(f'calling Wire.items[{key}].calc()')
            return Wire.items[key].calc()

    def load_wire_dict(dir, lines):
        [Wire(expression = line.split(" -> ")[0].split(" "), dest_port = line.split(" -> ")[1])
         for line in lines]

    load_wire_dict(DIR, quiz_input)

    a = get_port_value("a")
    
    # for wire in Wire.items.values():
    #     wire.value = x if wire.dest_port == "b" else None
    
    # print(x, get_port_value("a"), sep="\n")

    print(f'{a = }')
if __name__ == '__main__':
    main.main(solution, level='DEBUG')