import json


def get_total_chars(quiz_input:str) -> int:
    for s in quiz_input.split():
        print(s, len(s))
    return sum(len(s) for s in quiz_input.split())

def get_total_mem(quiz_input:str) -> int:
    return sum(len(eval(s)) for s in quiz_input)

def get_total_encoded(quiz_input:str) -> int:
    return sum(len(json.dumps(line)) for line in quiz_input)