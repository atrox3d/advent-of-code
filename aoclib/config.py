import json
import os
from dataclasses import dataclass

DEFAULT_JSON_PATH = f'{os.getcwd()}/config.json'

@dataclass
class Config:
    template_path: str

    @classmethod
    def from_json(cls, jsonpath=DEFAULT_JSON_PATH):
        with open(jsonpath, 'r') as fp:
            config = json.load(fp)
            return cls(**config)

