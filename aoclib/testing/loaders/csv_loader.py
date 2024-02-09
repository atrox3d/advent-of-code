import csv

import logging
logger = logging.getLogger(__name__)


def str_to_val(value):
    if value.isnumeric():
        value = int(value)
    elif value.lower() in ('true', 'false'):
        value = bool(value)
    elif value.lower() == 'none':
        value = None
    return value

def csv_loader(input_path):
    with open(input_path) as fp:
        reader = csv.reader(fp,)
        lines = [list(map(str.strip, line)) for line in reader]
        logger.debug(f'{lines = }')
        convert = [[str_to_val(value) for value in values] for values in lines]
        return convert