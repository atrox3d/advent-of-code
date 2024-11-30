from collections import defaultdict
import re
import pytest
from pathlib import Path

REGEX = r'^(\w+) to (\w+) = (\d+)$'

def parse_distances(quiz_input:str) -> tuple[str, str, int]:
    lines = [line for line in quiz_input.splitlines() if line]
    # print(lines)
    groups = [re.match(REGEX, line).groups() for line in lines]
    # print(groups)
    result = [(start, end, int(distance)) for start, end, distance in groups]
    # print(result)
    return result
    # return [(start, end, int(distance)) 
            # for start, end, distance in [re.match(REGEX, line).groups() 
            # for line in quiz_input if line]]

def build_map(distances:tuple[str,str,int]) -> dict[str, int]:
    maap = defaultdict(dict)
    for start, end, distance in distances:
        maap[start].update({end:distance})
        maap[end].update({start:distance})

    outmap = dict(maap)
    # print(outmap)
    return outmap

def get_city_list(distances:tuple[str,str,int]) -> list:
    # use a set to eliminate duplicates
    cities = {city for record in distances for city in record[:2]}
    # print(cities)
    return cities

def rpermute(cities:set):
    if len(cities) == 1:
        return [cities]
    
    perms = []
    for city in cities:
        for perm in rpermute([c for c in cities if c!=city]):
            ret = [city,  *perm]
            perms.append(ret)
    # print(perms)
    return perms

def get_routes(perms:list, maap:dict):
    routes = {}
    for perm in perms:
        # logger.debug(f'{perm = }')
        total = 0
        for start, end in zip(perm, perm[1:]):
            total += maap[start][end]
        routes[tuple(perm)] = total
    # print(routes)
    return routes
