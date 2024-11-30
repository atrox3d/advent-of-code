import json
try:
    import wiring
except:
    from . import wiring

def test_build_wires(circuit, gates):
    wires = wiring.build_wires(circuit)

    print(json.dumps(wires, indent=2))

    for port, value in wires.items():
        print(f'{port = }, {value = }')
        assert value == gates[port]

def test_wire2str(circuit, strwires):
    wires = wiring.build_wires(circuit)
    for wire in wires.items():
        port, gate = wire
        str_wire = wiring.wire2str(wire)
        assert strwires[port] == str_wire

def test_wire_values(circuit, signals):
    wires = wiring.build_wires(circuit)
    for port, gate in wires.items():
        signal = wiring.get_wire_value(port, wires)
        print(port, signal)
        assert signals[port] == signal
