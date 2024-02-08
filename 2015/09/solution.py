"""
https://adventofcode.com/2015/day/9
https://adventofcode.com/2015/day/9#part2
"""
import logging
import sys, os
import re, json
from pathlib import Path
from collections import defaultdict

sys.path.append(os.getcwd())
from aoclib import main

REGEX = r'^(\w+) to (\w+) = (\d+)$'
logger = logging.getLogger(__name__)
def solution(quiz_input):
    distances = [(start, end, int(distance)) for start, end, distance in 
                 [re.match(REGEX, line).groups() for line in quiz_input]]
    print(f'{distances = }')

    maap = defaultdict(list)
    for start, end, distance in distances:
        maap[start].append({end:distance})
    jmap = json.dumps(maap)
    print(f'{jmap = }')

    cities = [city for city in 
            #   [city for record in distances for city in record[:2]]
              {city for record in distances for city in record[:2]}
              ]
    print(f'{cities = }')

    '''
    Dublin -> London -> Belfast = 982
    London -> Dublin -> Belfast = 605
    London -> Belfast -> Dublin = 659
    Dublin -> Belfast -> London = 659
    Belfast -> Dublin -> London = 605
    Belfast -> London -> Dublin = 982
    '''
    import itertools
    product = list(itertools.product(cities, cities, cities,))
    print(f'{product = }')
    uniqueproduct = list((a, b, c) for a, b, c in product if a != b and a != c and b!= c)
    print(f'{uniqueproduct = }')
    

if __name__ == '__main__':
    LOGFILE = str(Path(sys.argv[0]).parent / Path(__file__).stem) + '.log'
    handlers = [
        logging.FileHandler(LOGFILE, mode='w'),
        logging.StreamHandler()
    ]
    main.main(solution, level='DEBUG', handlers=handlers)