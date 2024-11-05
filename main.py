from doctest import debug
import pytest

from aoclib import modules
from aoclib import data
from aoclib import options
from aoclib import commands

############## DELETE ###########################################
def deleteme_when_youre_done():
    part1 = modules.load_module_from_package('2015.01.part1')
    part1.solution(data.get_inputpath(part1))

    part2 = modules.load_module_from_path('2015/01/part2.py')
    part2.solution(data.get_inputpath(part2))

    pytest.main(['2015/01/part1.py', '2015/01/part2.py'])
############## DELETE ###########################################


def main():
    args = options.parse_args()

    parts = [args.part] if args.part else [1, 2]
    for part in parts:
        solution_path = data.get_solutionpath(args.year, args.day)
        solution_file = data.get_solutionfile(args.year, args.day, part)
        solution_package = data.get_solutionpackage(args.year, args.day, part)
        module = modules.load_module_from_path(solution_file)
        solution = module.solution
        inputpath = data.get_inputpath(module)

        if args.command == 'setup':
            commands.setup()
        elif args.command == 'run':
            commands.run()
        elif args.command == 'test':
            commands.test()
        else:
            raise SystemExit(f'unknown command {args.command}')
            exit()

if __name__ == "__main__":
    main()