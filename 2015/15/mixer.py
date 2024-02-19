def bestmixes(target, portions, max, level=None, cache=None):
    print(f'{target = }')
    cache = {} if cache is None else cache
    level = 0 if level is None else level
    level += 1
    if level > max: return None
    if target < 0: return None
    if target == 0: return []

    try:
        return cache[target]
    except:
        pass
    
    print(f'{level = }')

    combo = []
    for portion in portions:
        print(f'{portion = }')
        retcombos = bestmixes(target - portion, portions, max, level)
        print(f'{retcombos = }')
        if retcombos is not None:
            # for combo in retcombos:
            if combo is not None:
                combo = [*combo, portion]
                # combos.append(combo)
                try:
                    cache[target] = combo
                    print(cache)
                except:
                    pass
    return combo

def gencombos( target, column ):
    if column == 1:
        yield [target]
    else:
        print(f'for i in range( 0, target//column+1 ):')
        print(f'for i in range( 0, {target//column+1} ):')
        for i in range( 0, target//column+1 ):
            print(f'for row in gencombos( target-i*column, column-1 ):')
            print(f'for row in gencombos( {target-i*column}, {column-1} ):')
            for row in gencombos( target-i*column, column-1 ):
                yield row+[i]

for row in gencombos( 7, 3 ):
    print(row)
