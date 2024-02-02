import argparse

import helpers

def get_parser() -> argparse.ArgumentParser:
    # create parser
    parser = argparse.ArgumentParser(
        description="aoc parser"
    )

    # parser.add_argument('positional1')

    # parser.add_argument(
    #     # '-o'
    #     '-offset',
    #     '--offset',
    #     metavar='',
    #     type=str,
    #     help='offset',
    #     required=True
    # )
    # parser.add_argument('file', type=argparse.FileType('r'))
    # args = parser.parse_args()
    # print(args.file.readlines())
    # parser.add_argument('-i', '--input',
    #                     type=argparse.FileType('r', encoding='utf-8'), 
    #                     required=False,
    #                     default=str(helpers.INPUT_PATH)
    #                     )
    parser.add_argument('test_val', nargs='?')
    parser.add_argument('-p', '--print', action='store_true')
    parser.add_argument('-t', '--test',  action='store_true')
    parser.add_argument('-i', '--input_path', default=helpers.INPUT_PATH)
    return parser
