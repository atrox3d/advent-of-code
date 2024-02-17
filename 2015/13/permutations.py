items = ['Tristram', 'AlphaCentauri', 'Faerun', 'Norrath']
# , 'Snowdin', 'Straylight', 'Arbre', 'Tambi']
items = ['Belfast', 'London', 'Dublin', 4]
items = [1,2,3]

def rpermute(items):
    # print(f'{cities = }')
    if len(items) == 1:
        return [items]
    
    out = []
    for item in items:
        for res in rpermute([c for c in items if c!=item]):
            # print(f'{res = }')
            ret = [item,  *res]
            # print(f'{city = }')
            # print(f'{ret = }')
            out.append(ret)
    return out

x = rpermute(items)
print(x)
print(len(x))
# print(len(set(x)))
# print(permute(cities))
print([y for y in x if y[0] == 'Belfast'])
