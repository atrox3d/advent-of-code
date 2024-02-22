'''
3   0 0 0
    3 0 0
    2 1 0
    1 2 0
    0 3 0
    0 2 1
    0 1 2
    0 0 3
'''
verbose = False
def vprint(*args, **kwargs):
    if verbose:
        print(*args, **kwargs)

def rng(start, end, direction=None):
    if direction is None:
        direction = (end-start) // abs(end-start)
        if direction < 0:
            end, start = start, end
            start += 1
        else:
            end -= 1

    vprint(f'{start, end, direction = }')
    if end == start:
        yield end
    else:
        ret = rng(start, end -1, direction)
        vprint(f'{ret = }')
        if direction > 0:
            for val in ret:
                vprint(f'{val = }')
                # for r in [val] + [end]:
                vprint(f'yield {val=}')
                yield val
            yield end
        elif direction < 0:
            yield end
            for val in ret:
                vprint(f'{val = }')
                # for r in [val] + [end]:
                vprint(f'yield {val=}')
                yield val
                # for r in [end] + [val]:
                    # vprint(f'yield {r=}')
                    # yield r
            # else:
                # yield []


# print(subrange(5))
# print(add_range(3))

# print(rng(0, 2))
# print(rng(2, 0))
for x in rng(0, 5): print(f'{x = }')
print()
for x in rng(5, 0): print(f'{x = }')
print()
for x in rng(-3, 5): print(f'{x = }')
print()
for x in rng(5, -3): print(f'{x = }')
print()