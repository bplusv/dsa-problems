def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
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


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
