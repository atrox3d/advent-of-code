import logging

logger = logging.getLogger(__name__)


import csv
import json
from pathlib import Path


def get_loader(input_path):
    def json_loader(input_path):
        with open(input_path) as fp:
            data = json.load(fp)
            logger.debug(f'{data = }')
            for d in data:
                for k, v in d.items():
                    if '\n' in v:
                        d[k] = [line for line in v.split('\n') if line]
            logger.debug(f'{data = }')
            data = [tuple(item.values()) for item in data]
            logger.debug(f'{data = }')
        return data

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

    suffix = Path(input_path).suffix
    if suffix == '.json':
        logger.info(f'json loader')
        return json_loader
    elif suffix == '.csv':
        logger.info(f'csv loader')
        return csv_loader
    else:
        raise NotImplementedError(f'file type {suffix} not implemented')