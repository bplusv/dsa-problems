We can solve this problem in O(log(n)) if we first find the rotation pivot with a binary search in log(n) and then search with regular binary search and modulus operator on the left or right subarray.
Another approach to solving it without the extra search for the pivot is to add the necessary conditions to correctly discard the half of the array on each step in the binary search itself.

Time complexity: O(log(n))
Space complexity: O(1)
