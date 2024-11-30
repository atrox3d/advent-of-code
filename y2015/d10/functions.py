
def look_and_say(string: str, reps: int) -> int:
    for _ in range(reps):
        prev_char = ''
        count = 0
        result = ''
        for char in string:
            if char != prev_char:
                if prev_char != '':
                    result += f'{count}{prev_char}'
                    count = 0
            count += 1
            prev_char = char
        result += f'{count}{char}'
        string = result
        print(f'{_}:{result}:{len(result)}')

    return len(result)

def test_look_and_say():
    assert look_and_say('1', 5) == 6