import itertools

def get_mixes(spoons, ingredients):
    for mix in itertools.product(range(1, spoons+1), repeat=ingredients):
        yield mix
