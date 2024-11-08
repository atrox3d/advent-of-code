import re


REGEX1 = (
        r'^(?P<left>'           # 0
        r'(\w+)|'               # 1 2
        r'(\d+)|'               # 3 4
        r'(\w+) (\w+) (\w+)|'   # 5 6
        r'(\w+) (\w+)'          # 6 7
        r')'
        r' (->) '               # 8
        r'(?P<right>\w+)$'      # 9
)

REGEX2 = (
        r'^(\d+|\w+)*\s*'
        r'(AND|OR|NOT|LSHIFT|RSHIFT)*\s*(\d+|\w+)*'
        r' (->) '
        r'(\w+)$'
)

def split_lr(line: str) -> tuple[tuple]:
    '''
    returns a tuple containing (left, right) parts of the expression
    separated by ' -> '
    '''
    REGEX_LR = r'^(.+)\s->\s(.+$)'
    found = re.match(REGEX_LR, line)
    return found.groups()

def parse_gate(expr: str) -> tuple:
    '''
    returns a tuple containing possible lvalue, operator and rvalue
    tries to convert numeric values to integers, eg. a=10
    '''
    REGEX_EXPR = r'^(\d+|\w+)*\s*(AND|OR|NOT|LSHIFT|RSHIFT)*\s*(\d+|\w+)*'
    found = re.match(REGEX_EXPR, expr)
    groups = [int(item) if item is not None and item.isnumeric()
              else item
              for item in found.groups()]
    return groups
