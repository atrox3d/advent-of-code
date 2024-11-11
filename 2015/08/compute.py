import json


def get_total_chars(quiz_input:str) -> int:
    sumlens = sum(len(s) for s in quiz_input.split())
    return sumlens

def get_total_mem(quiz_input:str) -> int:
    sumlens = sum(len(eval(s)) for s in quiz_input.split())
    return sumlens

def get_total_encoded(quiz_input:str) -> int:
    return sum(len(json.dumps(line)) for line in quiz_input.split())