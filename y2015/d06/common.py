def parse_instruction(line: str):
    import re

    # instructions = re.compile(r'(\D+) (\d+),(\d+) (\D+) (\d+),(\d+)')
    instructions = re.compile(r'^(\w+) (\D*)(\d+),(\d+) (\w+) (\d+),(\d+)$')
    tokens = instructions.match(line)
    if tokens:
        match tokens.groups():
            case 'turn', onoff, startr, startc, 'through', endr, endc:
                start = int(startr), int(startc)
                end = int(endr), int(endc)
                onoff = onoff.strip()
                # onoff = 1 if onoff == 'on' else 0
                return 'turn', onoff, start, end
            
            case 'toggle', _, startr, startc, 'through', endr, endc:
                start = int(startr), int(startc)
                end = int(endr), int(endc)
                return 'toggle', None, start, end

            case _:
                raise ValueError(f'unrecognized pattern {tokens.groups()}')

    else:
        print(f'ERROR: no match: {line}')
        exit()

def strategy_part1(action: str, param: str, value: int) -> int:
    if action == 'turn':
        newvalue = 1 if param == 'on' else 0
        return newvalue
    elif action == 'toggle':
        return value ^ 1

def strategy_part2(action: str, param: str, value: int) -> int:
    if action == 'turn':
        offset = 1 if param == 'on' else -1
        value += offset
        return value if value >= 0 else 0
    elif action == 'toggle':
        return value + 2


def act(grid, action: str, param: str, start: tuple[int], end: tuple[int],
        strategy):
    for r in range(start[0], end[0]+1):
        for c in range(start[1], end[1]+1):
            grid[r][c] = strategy(action, param, grid[r][c])

