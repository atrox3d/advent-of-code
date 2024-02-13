cities = ['Tristram', 'AlphaCentauri', 'Faerun', 'Norrath']
# , 'Snowdin', 'Straylight', 'Arbre', 'Tambi']
cities = ['Belfast', 'London', 'Dublin', 4]

def rpermute(cities):
    # print(f'{cities = }')
    if len(cities) == 1:
        return [cities]
    
    out = []
    for city in cities:
        for res in rpermute([c for c in cities if c!=city]):
            # print(f'{res = }')
            ret = [city,  *res]
            # print(f'{city = }')
            # print(f'{ret = }')
            out.append((tuple(ret)))
    return tuple(out)

x = rpermute(cities)
print(x)
print(len(x))
# print(len(set(x)))
# print(permute(cities))
print([y for y in x if y[0] == 'Belfast'])
