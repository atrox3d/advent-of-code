def rng(start, end, direction=None):
    if direction is None:                   # only the first time
        direction = (
            (end-start) // abs(end-start)   # detect direction       
            )
        if direction < 0:                   # invert params if reverse
            end, start = start, end
            start += 1                      # exclude last element
        else:
            end -= 1                        # exclude last element

    if end == start:                        # base case
        yield end
    else:
        ret = rng(start, end-1, direction)  # recursive case
        if direction > 0:                   # use the right order
            for val in ret:                 # ret is a generator
                yield val                   # yield each element
            yield end                       # before the last
        elif direction < 0:
            yield end                       # yield the last first
            for val in ret:
                yield val                   # then everything else

if __name__ == '__main__':
    for x in rng(0, 5): print(f'{x = }')
    print()
    for x in rng(5, 0): print(f'{x = }')
    print()
    for x in rng(-3, 5): print(f'{x = }')
    print()
    for x in rng(5, -3): print(f'{x = }')
    print()