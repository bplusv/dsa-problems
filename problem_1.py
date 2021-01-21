def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       (int): Floored Square Root
    """
    assert number >= 0, 'Only square root of positive numbers are valid'
    start = 0
    end = number
    res = None
    while start <= end:
        middle = (start + end) // 2
        square = middle ** 2
        next_square = (middle + 1) ** 2
        if square <= number and next_square > number:
            res = middle
            break
        if square > number:
            end = middle - 1
        else:
            start = middle + 1
    return res


def test_function(test_case):
    test_input, test_expected = test_case
    try:
        test_actual = sqrt(test_input)
    except AssertionError:
        test_actual = AssertionError
    if test_actual == test_expected:
        print("Pass")
    else:
        print("Fail")


test_function((-75, AssertionError))
test_function((-1, AssertionError))
test_function((0, 0))
test_function((1, 1))
test_function((9, 3))
test_function((15, 3))
test_function((27, 5))
test_function((99, 9))
test_function((100, 10))
