def parse_reindeers(quiz_input):
    import re
    pattern = r'(?P<name>\w+) can fly (?P<speed>\d+) km/s for (?P<flytime>\d+) seconds,' \
            r' but then must rest for (?P<resttime>\d+) seconds.'
    data = {}
    for line in quiz_input:
        match = re.match(pattern, line)
        temp = match.groupdict()
        data[temp['name']] = {k:int(v) for k,v in temp.items() if k != 'name'}
    return data

def race1(finaltime, reindeers, print_step=False, print_result=False):
    for name, stats in reindeers.items():
        # a single unit of fly and rest
        fly_rest_block = stats['flytime'] + stats['resttime']
        # how many units until time
        complete_blocks = finaltime // fly_rest_block
        # how many seconds inside the last block
        remainder = finaltime % fly_rest_block
        # the remainder FLY part of the last block
        partial_block = min(remainder, stats['flytime'])
        distance = (complete_blocks * stats['speed'] * stats['flytime']) \
                    + (partial_block * stats['speed'])
        
        stats['distance'] = distance
        
        if print_step:
            print(f'{name = }')
            print(f'{fly_rest_block = }')
            print(f'{complete_blocks = }')
            print(f'{remainder = }')
            print(f'{partial_block = }')
            print(f'{distance = }')
            print()

    win_distance = 0
    winners = []
    for name, stats in reindeers.items():
        distance = stats['distance']
        if  distance > win_distance:
            winners = []
            win_distance = distance
            winners.append((name, distance))
        elif distance == win_distance:
            # tie
            winners.append((name, distance))
    
    if print_result:
        print(f'{finaltime = }')
        print(f'{winners = }')
        print(f'{win_distance = }')
        print()
    return winners

def race2(finaltime, reindeers):
    winner_name = None
    winner_points = 0

    for name, stats in reindeers.items():
        stats['points'] = 0
    
    for seconds in range(1, finaltime+1):
        winners = race1(seconds, reindeers)
        # print(f'{winners = }')
        for winner, distance in winners:
            reindeers[winner]['points'] += 1
            points = reindeers[winner]['points']
            # print(f'{seconds, winner, distance, points = }')
            if points > winner_points:
                winner_name = winner
                winner_points = points
    return winner_name, winner_points
