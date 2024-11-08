import logging
import ctypes

try:
    import regexprocess
except:
    from . import regexprocess


logger = logging.getLogger(__name__)

def build_wires(quiz_input: list[str]) -> dict:
    '''
    builds a dictionary with key = portname and value = expression tuple
    '''
    wires = {}
    for line in quiz_input:
        print(f'BUILDWIRES | {line = }')
        gate, port = regexprocess.split_lr(line)
        print(f'BUILDWIRES | {gate = }, {port = }')
        if wires.get(port, False):
            raise ValueError(f'multiple values for wire {port}')
        wires[port] = regexprocess.parse_gate(gate)
    return wires

def wire2str(wire: tuple[str, tuple]) -> str:
    '''
    prints the human format: p = a op b
    '''
    port, gate = wire
    match gate:
        case lvalue, None, None:
            return f'{port} = {lvalue}'
        case op, None, rvalue:
            return f'{port} = {op} {rvalue}'
        case lvalue, op, rvalue:
            return f'{port} = {lvalue} {op} {rvalue}'
        case _:
            raise ValueError(gate)

def get_wire_value(port:str, wires: dict[str, tuple], call_stack:list=None) -> int:
    if call_stack is None: call_stack = []
    stack_len = len(call_stack)
    # indent = '' * indent_level
    call_stack_pos = f'stack: [{stack_len}] '
    call_stack.append(stack_len)

    if isinstance(port, int):
        # nothing to solve, es. 123
        logger.debug(f'{call_stack_pos}{port = } is int, returning')
        return port
    
    gate = wires[port]
    if isinstance(gate, int):
        # nothing to solve, es. x -> 123
        logger.debug(f'{call_stack_pos}{port=} {gate = } is int, returning')
        return gate
    
    match gate:
        case lvalue, None, None:
            logger.debug(f'{call_stack_pos}match: {port} = {lvalue}')
            value = get_wire_value(lvalue, wires)
        
        case op, None, rvalue,:
            logger.debug(f'{call_stack_pos}match: {port} = {op} {rvalue}')
            match op:
                case 'NOT':
                    value = get_wire_value(rvalue, wires)
                    value = ctypes.c_uint16(~value).value
        
        case lvalue, op, rvalue:
            logger.debug(f'{call_stack_pos}match: {port} = {lvalue} {op} {rvalue}')
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
            raise ValueError(f'{call_stack_pos}{gate}')
    
    if isinstance(value, int):
        logger.debug(f'{call_stack_pos}updating wires[{port}] = {value}')
        wires[port] = value
    return value
