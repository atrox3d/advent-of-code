import json
import logging

logger = logging.getLogger(__name__)

# tests = [
#     {
#         'input': ['aaa'], 
#         'expected': {'nice': 1, 'naughty': 0},
#     },
#     {
#         'input': ['jchzalrnumimnmhp'], 
#         'expected': {'nice': 0, 'naughty': 1},
#     },
#     {
#         'input': ['dvszwmarrgswjxmb'], 
#         'expected': {'nice': 0, 'naughty': 1},
#     },
# ]

def create_json_tests(data, path):
    logger.debug(f'{path = }')
    logger.debug(f'{data = }')
    with open(path, 'w') as jf:
        json.dump(data, jf, indent=2)
