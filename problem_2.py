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
        arr(array), number(int): Input array to search and the target
    Returns:
        int: Index or -1
    """
    return _rotated_array_search(arr, number, 0, len(arr) - 1)


def linear_search(arr, number):
    for index, element in enumerate(arr):
        if element == number:
            return index
    return -1


def test_function(test_case):
    arr = test_case[0]
    number = test_case[1]
    if linear_search(arr, number) == rotated_array_search(arr, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[0, 1, 2, 3, 4, 5, 6, 7], 3])
