def sift_down(arr, i, n):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        sift_down(arr, largest, n)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        sift_down(arr, i, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sift_down(arr, 0, i)


def rearrange_digits(arr):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       arr(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    heap_sort(arr)
    res = [0, 0]
    curr = 0
    for i in range(len(arr) - 1, -1, -1):
        res[curr] = res[curr] * 10 + arr[i]
        curr = (curr + 1) % 2
    return res


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
