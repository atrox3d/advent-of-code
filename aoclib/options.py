import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('command', 
                        choices=['run', 'test', 'setup'])
    parser.add_argument('year', type=int)
    parser.add_argument('day', type=int)
    parser.add_argument('part', nargs='?', default=None)

    # path = parser.add_mutually_exclusive_group(required=True)
    # path.add_argument('--path')
    # path.add_argument('--package')
    # parser.add_argument('--part')

    options = parser.parse_args()
    options.day = f'{options.day:02d}'
    return options
