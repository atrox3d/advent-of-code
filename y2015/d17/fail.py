import itertools

example = 25, [20, 15, 10, 5, 5]
target, numbers = example

def reggnog(total:int, containers:list[int], portions=None) -> list[int]:

    if total < 0: return None
    
    if total == 0: 
        portions = portions if portions is not None else []
        return []
    
    print(total, containers)
    for idx, num in enumerate(containers):
        remainder = total - num
        delta = containers[0:idx] + containers[idx+1:]
        # print(f'{num=}, {delta=}')
        result = reggnog(remainder, delta)
        if result is not None:
            # print(f'return {[num, *result]}')
            return [num, *result]

def compute_eggnog():
    combos = []
    total, containers = example
    for idx, num in enumerate(containers):
        delta = containers[idx:idx+1] + containers[0:idx] + containers[idx+1:]
        
        print(f'{num = }, {delta = }')
        result = reggnog(total, delta)
        print(f' {result = }\n')

        # if result not in combos:
        combos.append(result)
    print(combos)

# compute_eggnog()
def perm():
    combos = set()
    for combo in itertools.permutations(numbers):
        print(combo)
        # print(combos)
        total = 0
        temp = []
        for num in combo:
            total += num
            if total < target:
                temp.append(num)
                continue
            if total == target:
                temp.append(num)
                combos.add(tuple(temp))
            break

    print(combos)

def nope():
    combos = set()
    numbers.sort()
    for i, num in enumerate(numbers):
        print(num)
        combo = [num]
        total = num
        for z, n in enumerate(numbers[0:i]+numbers[i+1:]):
            print(f'{total} + {n} = {total+n}')
            total += n
            if total < target:
                combo.append(n)
                continue
            if total == target:
                combo.append(n)
                combos.add(tuple(combo))
                print(combo)
                break
            print(f'{total} - {n} = {total-n}')
            total -= n
        print()
    print(combos)

