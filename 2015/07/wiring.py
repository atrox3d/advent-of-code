import logging

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
        print(f'LINE | {line}')
        gate, wid = regexprocess.split_lr(line)
        if wires.get(wid, False):
            raise ValueError(f'multiple values for wire {wid}')
        wires[wid] = regexprocess.parse_gate(gate)
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

def get_wire_value(wid:str, wires: dict[str, tuple], stack=[]) -> int:
    stack_len = len(stack)
    # indent = '' * indent_level
    stack_pos = f'stack: [{stack_len}] '
    stack.append(stack_len)

    if isinstance(wid, int):
        logger.debug(f'{stack_pos}{wid = } is int, returning')
        return wid
    
    gate = wires[wid]
    if isinstance(gate, int):
        logger.debug(f'{stack_pos}{wid=} {gate = } is int, returning')
        return gate
    
    match gate:
        case lvalue, None, None:
            logger.debug(f'{stack_pos}match: {wid} = {lvalue}')
            value = get_wire_value(lvalue, wires)
        
        case op, None, rvalue,:
            logger.debug(f'{stack_pos}match: {wid} = {op} {rvalue}')
            match op:
                case 'NOT':
                    value = ~get_wire_value(rvalue, wires)
        
        case lvalue, op, rvalue:
            logger.debug(f'{stack_pos}match: {wid} = {lvalue} {op} {rvalue}')
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
            raise ValueError(f'{stack_pos}{gate}')
    
    if isinstance(value, int):
        logger.debug(f'{stack_pos}updating wires[{wid}] = {value}')
        wires[wid] = value
    return value
