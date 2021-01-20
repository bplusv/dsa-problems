The problem can be solved by sorting the numbers and then creating the required 2 numbers in linear time.
A heap sort implementation is used, providing constant space for in-place sorting and linear time for the initial heapify.
The final scan on the sorted array is used to generate the 2 numbers in O(n). The heap sort O(nlog(n)) complexity dominates.

Time complexity: O(nlog(n))
Space complexity: O(1)
