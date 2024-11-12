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

