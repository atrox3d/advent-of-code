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
        
    reindeers = parse_reindeers(quiz_input)
    print(reindeers)

    finaltime = 2503
    windistance = 0
    winner = None
    for name, stats in reindeers.items():
        print(f'{name = }')

        fly_rest_block = stats['flytime'] + stats['resttime']
        complete_blocks = finaltime // fly_rest_block
        remainder = finaltime % fly_rest_block
        partial_block = 1 if remainder >= stats['flytime'] else 0
        distance = (complete_blocks + partial_block) * stats['speed'] * stats['flytime']
        if distance > windistance:
            windistance = distance
            winner = name
        
        print(f'{fly_rest_block = }')
        print(f'{complete_blocks = }')
        print(f'{partial_block = }')
        print(f'{distance = }')
        print()
    print(f'{finaltime = }')
    print(f'{winner = }')
    print(f'{windistance = }')


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
