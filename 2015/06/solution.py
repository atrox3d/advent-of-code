import logging

import main

logger = logging.getLogger(__name__)

def solution(quiz_input):
    """
    Because your neighbors keep defeating you in the holiday house 
    decorating contest year after year, you've decided to deploy 
    one million lights in a 1000x1000 grid.

    Furthermore, because you've been especially nice this year, 
    Santa has mailed you instructions on how to display the ideal 
    lighting configuration.

    Lights in your grid are numbered from 0 to 999 in each direction; 
    the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. 
    The instructions include whether to turn on, turn off, 
    or toggle various inclusive ranges given as coordinate pairs. 
    Each coordinate pair represents opposite corners of a rectangle, 
    inclusive; a coordinate pair like 0,0 through 2,2 therefore refers 
    to 9 lights in a 3x3 square. The lights all start turned off.

    To defeat your neighbors this year, all you have to do is set up 
    your lights by doing the instructions Santa sent you in order.

    For example:

    turn on 0,0 through 999,999 would turn on (or leave on) every light.
    toggle 0,0 through 999,0 would toggle the first line of 1000 lights, 
    turning off the ones that were on, and turning on the ones that were off.
    turn off 499,499 through 500,500 would turn off (or leave off) 
    the middle four lights.
    After following the instructions, how many lights are lit?
    """
    def parse_instruction(line: str):
        import re
        logger.debug(line)
        # instructions = re.compile(r'(\D+) (\d+),(\d+) (\D+) (\d+),(\d+)')
        instructions = re.compile(r'^(\w+) (\D*)(\d+),(\d+) (\w+) (\d+),(\d+)$')
        tokens = instructions.match(line)
        if tokens:
            logger.debug(f'{tokens.groups()}')
            match tokens.groups():
                case 'turn', onoff, startr, startc, 'through', endr, endc:
                    start = int(startr), int(startc)
                    end = int(endr), int(endc)
                    onoff = onoff.strip()
                    onoff = 1 if onoff == 'on' else 0
                    logger.debug(f'TURN {onoff!r} {start} -> {end}')
                    return 'turn', onoff, start, end
                
                case 'toggle', _, startr, startc, 'through', endr, endc:
                    start = int(startr), int(startc)
                    end = int(endr), int(endc)
                    logger.debug(f'TOGGLE {start} -> {end}')
                    return 'toggle', None, start, end

                case _:
                    raise ValueError(f'unrecognized pattern {tokens.groups()}')

        else:
            print(f'ERROR: no match: {line}')
            exit()

    def act(grid, action: str, param: str, start: tuple[int], end: tuple[int]):
        # logger.info(f'{action, param, start, end = }')
        for r in range(start[0], end[0]+1):
            for c in range(start[1], end[1]+1):
                if action == 'turn':
                    grid[r][c] = param
                elif action == 'toggle':
                    grid[r][c] ^= 1


    grid = [[0 for c in range(1000)] for r in range(1000)]
    for line in quiz_input:
        instruction = parse_instruction(line)
        act(grid, *instruction)
    # print(grid)
    result = sum([sum(r) for r in grid])
    print(result)
    return result

if __name__ == '__main__':
    main.main(solution, level='INFO')