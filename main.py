from doctest import debug
import pytest

from aoclib.modules import load_module_from_path
from aoclib.modules import load_module_from_package
from aoclib.data import get_inputpath, get_solutionpath, get_solutionpackage
from aoclib.options import parse_args
from aoclib.commands import run, test, setup

def deleteme_when_youre_done():
    part1 = load_module_from_package('2015.01.part1')
    part1.solution(get_inputpath(part1))

    part2 = load_module_from_path('2015/01/part2.py')
    part2.solution(get_inputpath(part2))

    pytest.main(['2015/01/part1.py', '2015/01/part2.py'])


def main():
    options = parse_args()

    parts = [options.part] if options.part else [1, 2]
    for part in parts:
        solution_path = get_solutionpath(options.year, options.day, part)
        solution_ckage = get_solutionpackage(options.year, options.day, part)
        module = load_module_from_path(solution_path)
        solution = module.solution
        inputpath = get_inputpath(module)

        if options.command == 'setup':
            setup()
        elif options.command == 'run':
            run()
        elif options.command == 'test':
            test()
        else:
            raise SystemExit(f'unknown command {options.command}')
            exit()

if __name__ == "__main__":
    main()