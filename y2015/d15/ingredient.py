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
def parse_ingredients(quiz_input:str) -> dict:
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
    
def get_mixes_product(spoons, ingredients, valid=lambda mix, spoons:sum(mix)==spoons):
    '''returns all possible combinations of n ingredients for a max total of spoons'''
    for mix in itertools.product(range(1, spoons), repeat=ingredients):
        if valid(mix, spoons):
            yield mix

def get_mixes(spoons, ingredients, *args, func=get_mixes_product, **kwargs):
    return func(spoons, ingredients)

def get_property_names(ingredients:dict, *exclude) -> list:
    names = []
    for prop in ingredients.values():
        for name in prop:
            if name not in names and name not in exclude:
                names.append(name)
    return names

def get_property_score(property_name:str, mix:tuple, ingredients:dict, print_values=False) -> int:
    '''sum of product of quantity and property value of each ingredient'''
    property_score = 0
    for ingredient_quantity, properties in zip(mix, ingredients.values()):
        property_value = int(properties[property_name])
        property_product = ingredient_quantity * property_value
        property_score += property_product
        if print_values:
            print(f'get_property_score: {property_name=}, {property_value=}, {ingredient_quantity=}, {property_product=}, {property_score=}')
    return property_score

def find_calories(mixes:list, ingredients:dict, target):
    for mix in mixes:
        calories = get_property_score('calories', mix, ingredients)
        # print(mix, calories)
        if calories == target:
            # 1 is needed for product
            total = 1
            for property_name in get_property_names(ingredients, 'calories'):
                property_score = get_property_score(property_name, mix, ingredients)
                property_score = 0 if property_score < 0 else property_score
                total *= property_score
                # print(f'{mix=}, {property_score=}, {total=}, {max=}\n')
            # /for property_name in ing.get_property_names(ingredients, 'calories'):
            if total > 0:
                yield total, calories
    # /for mix in mixes

def get_scores(mixes:list, ingredients:dict, *exclude):
    for mix in mixes:
        # 1 is needed for product
        total = 1
        for property_name in get_property_names(ingredients, *exclude):
            property_score = get_property_score(property_name, mix, ingredients)
            property_score = 0 if property_score < 0 else property_score
            total *= property_score
            print(f'{exclude=}, {mix=}, {property_name=}, {property_score=}, {total=}\n')
        # /for property_name in ing.get_property_names(ingredients, 'calories'):
        yield total
    # /for mix in mixes

def get_max_score(mixes:list, ingredients:dict, *exclude):
    max = 0
    for total in get_scores(mixes, ingredients, *exclude):
        max = total if total > max else max
        print(f'{total = }, {max = }\n')
    return max # 222870

if __name__ == '__main__':
    for mix in get_mixes(10, 4):
        print(mix)