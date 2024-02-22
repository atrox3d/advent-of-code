def rng(start, end, direction=None):
    # detect direction on the first call
    if direction is None:
        direction = (end-start) // abs(end-start)
        # invert start, end if reverse
        if direction < 0:
            end, start = start, end
            # non inclusive of last element
            start += 1
        else:
            # non inclusive of last element
            end -= 1

    # base case
    if end == start:
        yield end
    else:
        # recursive case, ret is a generator
        ret = rng(start, end -1, direction)
        # yield elements in the right order
        if direction > 0:
            for val in ret:
                yield val
            yield end
        elif direction < 0:
            yield end
            for val in ret:
                yield val

if __name__ == '__main__':
    for x in rng(0, 5): print(f'{x = }')
    print()
    for x in rng(5, 0): print(f'{x = }')
    print()
    for x in rng(-3, 5): print(f'{x = }')
    print()
    for x in rng(5, -3): print(f'{x = }')
    print()