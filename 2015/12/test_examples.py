import pytest

try:
    from calc import find_numbers
except:
    from .calc import find_numbers


@pytest.mark.parametrize(
        'data, total', [
            ([1,2,3], 6),
            ({"a":2,"b":4}, 6),
            ([[[3]]], 3),
            ({"a":{"b":4},"c":-1}, 3),
            ({"a":[-1,1]}, 0),
            ([-1,{"a":1}], 0),
            ([], 0),
            ({}, 0),
        ]
)
def test_example_part1(data, total):
    assert total == sum(find_numbers(data))

@pytest.mark.parametrize(
        'data, total', [
            ([1,2,3], 6),
            ([1,{"c":"red","b":2},3] , 4),
            ({"d":"red","e":[1,2,3,4],"f":5}, 0),
            ([1,"red",5] , 6),
        ]
)
def test_example_part2(data, total):
    assert total == sum(find_numbers(data, skip='red'))
