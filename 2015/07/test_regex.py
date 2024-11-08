
try:
    import regexprocess
except:
    from . import regexprocess


def test_parse_gate(circuit, gates):
    for line in circuit:
        str_gate, port = regexprocess.split_lr(line)
        gate = regexprocess.parse_gate(str_gate)
        assert gate == gates[port]


def test_split_lr(circuit, gate_ports):
    for line in circuit:
        gate, port = regexprocess.split_lr(line)
        assert gate == gate_ports[port]
