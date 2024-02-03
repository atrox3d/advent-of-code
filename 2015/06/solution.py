import logging
import sys, os

sys.path.append(os.getcwd())
from aoclib import main

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

--- Part Two ---
    You just finish implementing your winning light pattern when you realize you 
    mistranslated Santa's message from Ancient Nordic Elvish.

    The light grid you bought actually has individual brightness controls;
    each light can have a brightness of zero or more. The lights all start at zero.

    The phrase turn on actually means that you should increase the brightness
    of those lights by 1.

    The phrase turn off actually means that you should decrease the brightness 
    of those lights by 1, to a minimum of zero.

    The phrase toggle actually means that you should increase the brightness 
    of those lights by 2.

    What is the total brightness of all lights combined after following Santa's 
    instructions?

    For example:

    turn on 0,0 through 0,0 would increase the total brightness by 1.
    toggle 0,0 through 999,999 would increase the total brightness by 2000000.    

    """
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

    grid = [[0 for c in range(1000)] for r in range(1000)]
    for line in quiz_input:
        instruction = parse_instruction(line)
        act(grid, *instruction, strategy_part2)
    result = sum([sum(r) for r in grid])
    print(result)
    return result

if __name__ == '__main__':
    main.main(solution, level='INFO')