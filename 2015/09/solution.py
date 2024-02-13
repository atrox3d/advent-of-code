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

# def build_map(distances):
#     maap = defaultdict(list)
#     for start, end, distance in distances:
#         maap[start].append({end:distance})
#         maap[end].append({start:distance})
#     return maap

def get_city_list(distances):
    # use a set to eliminate duplicates
    cities = {city for record in distances for city in record[:2]}
    return cities

def rpermute(cities):
    if len(cities) == 1:
        return [cities]
    
    perms = []
    for city in cities:
        for perm in rpermute([c for c in cities if c!=city]):
            ret = [city,  *perm]
            perms.append(ret)
    return perms


def get_routes(perms, distances):
    # routes = {'from': 'london', 'to': 'belfast', 'dist': 100}
    routes = []
    for perm in perms:
        print(f'{perm = }')
        # routes[perm] = 0
        total = 0
        for segment in zip(perm, perm[1:]):
            print(f'{segment = }')
            for start, end, dist in distances:
                if segment == (start, end) or segment == (end, start):
                    print(segment, dist)
                    total += dist
        print(f'{total = }')
        routes.append([*perm, total])


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
    print(f'{distances = }')
    cities = get_city_list(distances)
    print(f'{cities = }')
    # exit()
    print()
    permutations = rpermute(cities)
    
    routes = get_routes(permutations, distances)
    print(routes)


if __name__ == '__main__':
    LOGFILE = str(Path(sys.argv[0]).parent / Path(__file__).stem) + '.log'
    handlers = [
        logging.FileHandler(LOGFILE, mode='w'),
        logging.StreamHandler()
    ]
    main.main(solution, level='DEBUG', handlers=handlers)