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

bestmixes(10, 4, 4)