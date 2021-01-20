def get_min_max(arr):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       arr(list): list of integers containing one or more integers
    Returns:
        (int, int): A tuple of min and max numbers.
    """
    if len(arr) == 0:
        return None, None
    min_number = max_number = arr[0]
    for number in arr:
        if number < min_number:
            min_number = number
        if number > max_number:
            max_number = number
    return min_number, max_number


def test_function(test_case):
    test_input, test_expected = test_case
    test_actual = get_min_max(test_input)
    if test_actual == test_expected:
        print("Pass")
    else:
        print("Fail")


test_function(([], (None, None)))
test_function(([0], (0, 0)))
test_function(([-5], (-5, -5)))
test_function(([7], (7, 7)))
test_function(([9, 0, -4], (-4, 9)))
test_function(([-5, -7, 0, 4, 5, -1, -2], (-7, 5)))
test_function(([3, 5, 8, 1, 0, 9, 2, 4, 7, 6], (0, 9)))
test_function(([58, 73, 82, 49, 52, 76, 77, 61, 37, 67, 40, 48, 40, 51, 73, 32, 64], (32, 82)))
test_function(([-44, -44, -44], (-44, -44)))
test_function(([99, 99, 99, 99], (99, 99)))
test_function(([0, 0, 0, 0], (0, 0)))
