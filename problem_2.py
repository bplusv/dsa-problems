def _rotated_array_search(arr, number, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    if arr[middle] == number:
        return middle
    if left < middle and arr[left] < arr[middle]:
        if number >= arr[left] and number < arr[middle]:
            return _rotated_array_search(arr, number, left, middle - 1)
        else:
            return _rotated_array_search(arr, number, middle + 1, right)
    else:
        if number > arr[middle] and number <= arr[right]:
            return _rotated_array_search(arr, number, middle + 1, right)
        else:
            return _rotated_array_search(arr, number, left, middle - 1)


def rotated_array_search(arr, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
        arr(list), number(int): Input array to search and the target
    Returns:
        (int): Index or -1
    """
    return _rotated_array_search(arr, number, 0, len(arr) - 1)


def test_function(test_case):
    test_input, test_expected = test_case
    test_actual = rotated_array_search(*test_input)
    if test_actual == test_expected:
        print("Pass")
    else:
        print("Fail")


test_function((([6, 7, 8, 9, 10, 1, 2, 3, 4], 6), 0))
test_function((([6, 7, 8, 9, 10, 1, 2, 3, 4], 1), 5))
test_function((([6, 7, 8, 1, 2, 3, 4], 8), 2))
test_function((([6, 7, 8, 1, 2, 3, 4], 1), 3))
test_function((([6, 7, 8, 1, 2, 3, 4], 10), -1))
test_function((([0, 1, 2, 3, 4, 5, 6, 7], 3), 3))
test_function((([], 7), -1))
test_function((([1], 1), 0))
