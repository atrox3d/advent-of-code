import logging

from .loaders.csv_loader import csv_loader
from .loaders.json_loader import json_loader

logger = logging.getLogger(__name__)


from pathlib import Path

def str_to_val(value):
    if value.isnumeric():
        value = int(value)
    elif value.lower() in ('true', 'false'):
        value = bool(value)
    elif value.lower() == 'none':
        value = None
    return value

def get_loader(input_path):

    suffix = Path(input_path).suffix
    if suffix == '.json':
        logger.info(f'json loader')
        return json_loader
    elif suffix == '.csv':
        logger.info(f'csv loader')
        return csv_loader
    else:
        raise NotImplementedError(f'file type {suffix} not implemented')