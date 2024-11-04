from pathlib import Path

from aoclib.modules import load_module_from_path
from aoclib.modules import load_module_from_package

part1 = load_module_from_package('2015.01.part1')
part1.solution()

part2 = load_module_from_path('2015/01/part2.py')
part2.solution()
