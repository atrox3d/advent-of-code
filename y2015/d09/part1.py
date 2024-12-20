"""
https://adventofcode.com/2015/day/9
https://adventofcode.com/2015/day/9#part2
"""
import logging
import sys, os
import re, json
from pathlib import Path
from collections import defaultdict

# sys.path.append(os.getcwd())
# from aoclib import main

try:
    import functions
except:
    from . import functions

logger = logging.getLogger(__name__)

def solve(quiz_input):
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
    distances = functions.parse_distances(quiz_input)
    logger.debug(f'{distances = }\n')

    maap = functions.build_map(distances)
    logger.debug(f'{maap = }\n')
    
    cities = functions.get_city_list(distances)
    logger.debug(f'{cities = }\n')

    permutations = functions.rpermute(cities)
    logger.debug(f'{permutations = }\n')
    
    routes = functions.get_routes(permutations, maap)
    logger.debug(f'{routes = }')

    result = min(routes.values())
    print(result)
    return result


def solution(input_path):
    '''called from aoc/main.py'''

    print(f'open {input_path}')
    with open(input_path) as fp:
        input_text = fp.read()
    
    print(f'call solve <input_text>')
    result = solve(input_text)
    print(f'{result = }')
    print(f'end solution')



# if __name__ == '__main__':
#     LOGFILE = str(Path(sys.argv[0]).parent / Path(__file__).stem) + '.log'
#     handlers = [
#         logging.FileHandler(LOGFILE, mode='w'),
#         logging.StreamHandler()
#     ]
#     main.main(solution, level='INFO', handlers=handlers)
