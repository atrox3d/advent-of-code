"""
https://adventofcode.com/2015/day/14
https://adventofcode.com/2015/day/14#part2
"""
import logging
import sys, os
import re, json
from pathlib import Path

sys.path.append(os.getcwd())
from aoclib import main

logger = logging.getLogger(__name__)

def solution(quiz_input):
    '''
    --- Day 14: Reindeer Olympics ---
This year is the Reindeer Olympics! Reindeer can fly at high speeds, 
but must rest occasionally to recover their energy. 
Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) 
or resting (not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

- Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
- Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

- After one second, Comet has gone 14 km, while Dancer has gone 16 km. 
- After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. 

- On the eleventh second, Comet begins resting (staying at 140 km), 
  and Dancer continues on for a total distance of 176 km. 
- On the 12th second, both reindeer are resting. 

- They continue to rest until the 138th second, 
  when Comet flies for another ten seconds. 

- On the 174th second, Dancer flies for another 11 seconds.

- In this example, after the 1000th second, both reindeer are resting, 
  and Comet is in the lead at 1120 km 
  (poor Dancer has only gotten 1056 km by that point). 

- So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), 
after exactly 2503 seconds, what distance has the winning reindeer traveled?

--- Part Two ---
Seeing how reindeer move in bursts, Santa decides he's not pleased with 
the old scoring system.

- Instead, at the end of each second, he awards one point to the reindeer 
  currently in the lead.

- (If there are multiple reindeer tied for the lead, they each get one point.) 

He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, 
- Dancer is in the lead and gets one point. 
  - He stays in the lead until several seconds into Comet's second burst: 

- after the 140th second, Comet pulls into the lead and gets his first point. 

- Of course, since Dancer had been in the lead for the 139 seconds before that, 
  he has accumulated 139 points by the 140th second. 

- After the 1000th second, 
    - Dancer has accumulated 689 points, 
    - while poor Comet, our old champion, only has 312. 

- So, with the new scoring system, Dancer would win 
  (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), 
after exactly 2503 seconds, how many points does the winning reindeer have?
'''
    def parse_reindeers(quiz_input):
        import re
        pattern = r'(?P<name>\w+) can fly (?P<speed>\d+) km/s for (?P<flytime>\d+) seconds,' \
                r' but then must rest for (?P<resttime>\d+) seconds.'
        data = {}
        for line in quiz_input:
            match = re.match(pattern, line)
            temp = match.groupdict()
            data[temp['name']] = {k:int(v) for k,v in temp.items() if k != 'name'}
        return data

    def race1(finaltime, reindeers, print_step=False, print_result=True):
        windistance = 0
        winner = None
        for name, stats in reindeers.items():

            fly_rest_block = stats['flytime'] + stats['resttime']
            complete_blocks = finaltime // fly_rest_block
            remainder = finaltime % fly_rest_block
            partial_block = 1 if remainder >= stats['flytime'] else 0
            distance = (complete_blocks + partial_block) * stats['speed'] * stats['flytime']
            if distance > windistance:
                windistance = distance
                winner = name
            if print_step:
                print(f'{name = }')
                print(f'{fly_rest_block = }')
                print(f'{complete_blocks = }')
                print(f'{partial_block = }')
                print(f'{distance = }')
                print()
        if print_result:
            print(f'{finaltime = }')
            print(f'{winner = }')
            print(f'{windistance = }')
            print()
        return windistance

    def race2(finaltime, reindeers):
        for name, stats in reindeers.items():
            stats['points'] = 0
        print(reindeers)

        for seconds in range(1, finaltime+1):
            for name, stats in reindeers.items():
                speed, fly, rest, prevpoints = stats.values()
                block = fly+rest
                remainder = seconds % block
                points = prevpoints
                if remainder <= fly:
                    points = prevpoints + 1
                logger.info(f'{seconds}:{name}: {block=}, {remainder=}, {fly=}::{prevpoints=}->{points=}')
                reindeers[name]['points'] = points


    reindeers = parse_reindeers(quiz_input)
    print(reindeers)

    finaltime = 2503
    
    solution1 = race1(finaltime, reindeers)
    solution2 = race2(1000, reindeers)
    print(reindeers)
    
    return solution1, solution2


if __name__ == '__main__':
    LOGFILE = str(Path(sys.argv[0]).parent / Path(__file__).stem) + '.log'
    handlers = [
        logging.FileHandler(LOGFILE, mode='w'),
        logging.StreamHandler()
    ]
    main.main(
                solution, 
                input_param=None,
                test_input=None,
                test_expected=None, 
                level='INFO', 
                handlers=handlers
            )
