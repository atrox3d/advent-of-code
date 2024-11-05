import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('command', 
                        choices=['run', 'test', 'setup'])
    parser.add_argument('year', type=int)
    parser.add_argument('day', type=int)
    parser.add_argument('part', nargs='?', default=None,
                        type=int, choices=[1, 2])

    options = parser.parse_args()
    options.day = f'{options.day:02d}'
    return options
