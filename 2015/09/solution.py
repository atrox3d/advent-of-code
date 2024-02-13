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

def parse_distances(quiz_input):
    return [(start, end, int(distance)) for start, end, distance in 
                 [re.match(REGEX, line).groups() for line in quiz_input]]

def build_map(distances):
    maap = defaultdict(list)
    for start, end, distance in distances:
        maap[start].append({end:distance})
        maap[end].append({start:distance})
    return maap

def get_city_list(distances):
    cities = [city for city in 
            #   [city for record in distances for city in record[:2]]
              {city for record in distances for city in record[:2]}
              ]
    return cities

def rpermute(cities):
    # print(f'{cities = }')
    if len(cities) == 1:
        return [cities]
    
    out = []
    for city in cities:
        for res in rpermute([c for c in cities if c!=city]):
            # print(f'{res = }')
            ret = [city,  *res]
            # print(f'{city = }')
            # print(f'{ret = }')
            out.append((tuple(ret)))
    return tuple(out)


def solution(quiz_input):
    distances = parse_distances(quiz_input)
    # logger.info(f'{distances = }')
    '''
    London Dublin 464
    London Belfast 518
    Dublin Belfast 141

    Dublin -> London -> Belfast = 982
    Dublin -> Belfast -> London = 659
    London -> Dublin -> Belfast = 605
    London -> Belfast -> Dublin = 659
    Belfast -> Dublin -> London = 605
    Belfast -> London -> Dublin = 982
    '''
    print(distances)
    cities = get_city_list(distances)
    print(cities)
    print()
    permutations = rpermute(cities)
    for perm in permutations:
        print(perm)

if __name__ == '__main__':
    LOGFILE = str(Path(sys.argv[0]).parent / Path(__file__).stem) + '.log'
    handlers = [
        logging.FileHandler(LOGFILE, mode='w'),
        logging.StreamHandler()
    ]
    main.main(solution, level='DEBUG', handlers=handlers)