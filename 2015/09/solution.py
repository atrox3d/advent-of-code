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
    return [(start, end, int(distance)) 
            for start, end, distance in [re.match(REGEX, line).groups() 
            for line in quiz_input]]

def build_map(distances):
    '''
    x = {'london':{'dublin':15,'belfast':100}}
    x['london']
    {'dublin': 15, 'belfast': 100}
    x['london']['dublin']
    15
    '''
    maap = defaultdict(dict)
    # maap = {}
    for start, end, distance in distances:
        maap[start].update({end:distance})
        maap[end].update({start:distance})
    return dict(maap)

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

def get_routes(perms, maap):
    routes = {}
    for perm in perms:
        logger.debug(f'{perm = }')
        total = 0
        for start, end in zip(perm, perm[1:]):
            logger.debug(f'{start, end = }')
            logger.debug(f'{maap[start][end] = }')
            total += maap[start][end]
        logger.debug(f'{total = }')
        routes[tuple(perm)] = total
    return routes


def solution(quiz_input):
    '''
    --- Day 9: All in a Single Night ---
    Every year, Santa manages to deliver all of his presents 
    in a single night.

    This year, however, he has some new locations to visit; 
    his elves have provided him the distances between every pair 
    of locations. He can start and end at any two (different) 
    locations he wants, but he must visit each location exactly once. 
    What is the shortest distance he can travel to achieve this?

    For example, given the following distances:

    London to Dublin = 464
    London to Belfast = 518
    Dublin to Belfast = 141
    
    The possible routes are therefore:

    Dublin -> London -> Belfast = 982
    London -> Dublin -> Belfast = 605
    London -> Belfast -> Dublin = 659
    Dublin -> Belfast -> London = 659
    Belfast -> Dublin -> London = 605
    Belfast -> London -> Dublin = 982
    The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

    What is the distance of the shortest route? 141
    '''
    distances = parse_distances(quiz_input)
    logger.info(f'{distances = }\n')

    maap = build_map(distances)
    logger.info(f'{maap = }\n')
    
    cities = get_city_list(distances)
    logger.info(f'{cities = }\n')

    permutations = rpermute(cities)
    logger.info(f'{permutations = }\n')
    
    routes = get_routes(permutations, maap)
    logger.info(f'{routes = }')

    return min(routes.values())

if __name__ == '__main__':
    LOGFILE = str(Path(sys.argv[0]).parent / Path(__file__).stem) + '.log'
    handlers = [
        logging.FileHandler(LOGFILE, mode='w'),
        logging.StreamHandler()
    ]
    main.main(solution, level='INFO', handlers=handlers)