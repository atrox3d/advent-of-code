import logging
import sys, os

print(sys.path)
print(os.getcwd())
sys.path.append(os.getcwd())

from aoclib import main

logger = logging.getLogger(__name__)

def solution(quiz_input):
    """
    """
    return None

if __name__ == '__main__':
    main.main(solution, level='DEBUG')
