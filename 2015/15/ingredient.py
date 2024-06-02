import itertools
'''
    For instance, suppose you have these two ingredients:

    - Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
    - Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

    - Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon 
    (because the amounts of each ingredient must add up to 100) 
    would result in a cookie with the following properties:

    A capacity of 44*-1 + 56*2 = 68
    A durability of 44*-2 + 56*3 = 80
    A flavor of 44*6 + 56*-2 = 152
    A texture of 44*3 + 56*-1 = 76

    Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) 
    results in a total score of 62842880, 
    which happens to be the best score possible given these ingredients. 
    If any properties had produced a negative total, 
    it would have instead become zero, causing the whole score to multiply to zero.

'''
def load_ingredients(quiz_input:str) -> dict:
    import re
    pattern = r'(?P<name>\w+): capacity (?P<capacity>-?\d+), '\
            r'durability (?P<durability>-?\d+), flavor (?P<flavor>-?\d+), '\
            r'texture (?P<texture>-?\d+), calories (?P<calories>-?\d+)'
    ingredients = {}
    for line in quiz_input.splitlines():
        match = re.match(pattern, line)
        temp = match.groupdict()
        ingredients[temp['name']] = {k:int(v) for k, v in temp.items() if k != 'name'}
    return ingredients

def get_mixes(spoons, ingredients):
    '''returns all possible combinations of n ingredients for a max total of spoons'''
    for mix in itertools.product(range(1, spoons+1), repeat=ingredients):
        yield mix

def get_property_names(ingredients:dict) -> list:
    return [name for name in list(ingredients.values())[0]]

def get_property_score(property:str, qty:int, ingredients:dict) -> int:
    score = sum([props[property] * qty  for name, props in ingredients.items()])
    return score
