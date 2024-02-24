def bestmixes(spoons, portions):
    recipe = []
    for spoon in range(spoons+1):
        # for portion in range(portions):
        recipe.append((spoons-spoon, spoon))
    
    return recipe

recipe = bestmixes(5, 2)

print(recipe)
