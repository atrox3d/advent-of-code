import json
import logging

logger = logging.getLogger(__name__)

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