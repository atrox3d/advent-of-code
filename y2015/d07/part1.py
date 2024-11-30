from dataclasses import dataclass
import logging
import sys, os
import re, json
from pathlib import Path
import pytest

try:
    import wiring
except:
    from . import wiring

# sys.path.append(os.getcwd())
# from aoclib import main

logger = logging.getLogger(__name__)



def solve(quiz_input):
    '''
    '''
    # pass_test = { 'd': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079, 'x': 123, 'y': 456    }
    # zero = {k:0 for k in pass_test}
    wires = wiring.build_wires(quiz_input)
    for wire in wires.items():
        print(wiring.wire2str(wire))
    
    value = wiring.get_wire_value('a', wires)
    # value = wiring.get_wire_value('a', wires)
    print(value)
    return value

def solution(input_path):
    '''called from aoc/main.py'''

    with open(input_path) as fp:
        input_text = fp.readlines()
    
    return solve(input_text)


def test_solution_circuit_fixture(circuit):
    print(circuit)

def test_solution_signals_fixture(signals):
    print(signals)

# @pytest.mark.parametrize(
#         'circuit, expected', [
#             (TEST_CIRCUIT, EXPECTED_SIGNALS),
#         ]
# )
# def test_solution_2015_07_1(circuit, expected):
#     '''
#     '''
#     wires = wiring.build_wires(circuit)
#     print(json.dumps(wires, indent=2))
#     # for wire in wires.items():
#         # print(wiring.wire2str(wire))
    
#     # value = wiring.get_wire_value('a', wires)

#     for wire, value in wires.items():
#         assert expected[wire] == wiring.get_wire_value(wire, wires)


if __name__ == '__main__':
    handlers = [
        logging.FileHandler(
            str(Path(sys.argv[0]).parent / Path(__file__).stem) + '.log',
            mode='w'
            ),
        logging.StreamHandler()
    ]
    # main.main(solution, level='DEBUG', handlers=handlers)
