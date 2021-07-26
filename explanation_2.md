We solve this problem in O(log(n)) using a tweaked binary search function. Using the fact that in a sorted rotated array 
the half of the array will alweys be sorted in ascending order, we can decide which half of the array to discard for each step.

Time complexity: O(log(n))
Space complexity: O(1)
