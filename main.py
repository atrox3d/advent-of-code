import pytest

from aoclib.modules import load_module_from_path
from aoclib.modules import load_module_from_package
from aoclib.data import get_inputpath
from aoclib.options import parse_args

def nope():
    part1 = load_module_from_package('2015.01.part1')
    part1.solution(get_inputpath(part1))

    part2 = load_module_from_path('2015/01/part2.py')
    part2.solution(get_inputpath(part2))

    pytest.main(['2015/01/part1.py', '2015/01/part2.py'])


def main():
    options = parse_args()
    print(options)

    if options.command == 'setup':
        pass
    elif options.command == 'run':
        pass
    elif options.command == 'test':
        pass
    else:
        raise SystemExit(f'unknown command {options.command}')
    exit()

if __name__ == "__main__":
    main()