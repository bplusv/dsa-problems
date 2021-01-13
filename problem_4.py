def sort_012(arr):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       arr(list): List to be sorted
    """
    n = len(arr)
    pos0 = 0
    pos2 = n - 1
    i = 0
    while i <= pos2:
        if arr[i] == 0:
            arr[pos0], arr[i] = arr[i], arr[pos0]
            pos0 += 1
            i += 1
        elif arr[i] == 2:
            arr[pos2], arr[i] = arr[i], arr[pos2]
            pos2 -= 1
        else:
            i += 1
    return arr


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
