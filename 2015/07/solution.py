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
import pathlib, sys, os
sys.path.append(os.getcwd())
from aoclib import main



def read(dir, teststr):
    with open(dir / "input.txt") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    list(map(lambda r: Wire(r.split(" -> ")[0].split(" "), r.split(" -> ")[1]), s))


class Wire:
    items = {}

    def __init__(self, inp, out):
        self.output = out
        self.inp = inp + ["", ""]
        self.__class__.items[out] = self
        self.val = None

    def calc(self):
        if self.val is not None:
            return self.val
        elif self.inp[1] == "AND":
            self.val = v(self.inp[0]) & v(self.inp[2])
        elif self.inp[1] == "OR":
            self.val = v(self.inp[0]) | v(self.inp[2])
        elif self.inp[1] == "LSHIFT":
            self.val = v(self.inp[0]) << v(self.inp[2])
        elif self.inp[1] == "RSHIFT":
            self.val = v(self.inp[0]) >> v(self.inp[2])
        elif self.inp[0] == "NOT":
            self.val = ~v(self.inp[1])
        else:
            self.val = v(self.inp[0])
        return self.val


def v(key):
    try:
        return int(key)
    except:
        return Wire.items[key].calc()

def solution(quiz_input):
    teststr = """"""
    DIR = pathlib.Path(__file__).parent.absolute()
    read(DIR, teststr)
    x = v("a")
    for wire in Wire.items.values():
        wire.val = x if wire.output == "b" else None
    print(x, v("a"), sep="\n")

if __name__ == '__main__':
    main.main(solution, level='INFO')