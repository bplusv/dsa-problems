def get_min_max(arr):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
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
    output = get_min_max(test_case[0])
    solution = test_case[1]
    if output == solution:
        print("Pass")
    else:
        print("Fail")


test_function([[3, 5, 8, 1, 0, 9, 2, 4, 7, 6], (0, 9)])
test_function([[58, 73, 82, 49, 52, 76, 77, 61, 37, 67, 40, 48, 40, 51, 73, 32, 64], (32, 82)])
