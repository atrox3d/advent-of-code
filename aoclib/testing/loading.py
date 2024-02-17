import logging

from .loaders.csv_loader import csv_loader
from .loaders.json_loader import json_loader
from ..helpers.datainput import get_input

logger = logging.getLogger(__name__)


from pathlib import Path

def get_loader(input_path):

    suffix = Path(input_path).suffix
    if suffix == '.json':
        logger.info(f'json loader')
        return json_loader
    elif suffix == '.csv':
        logger.info(f'csv loader')
        return csv_loader
    elif suffix == '.txt':
        return get_input
    else:
        raise NotImplementedError(f'file type {suffix!r} not implemented')