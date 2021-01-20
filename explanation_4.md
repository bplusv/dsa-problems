We can solve this problem using two pointers, one at the start and another at the end of the list. We keep track of where the next '0' will go from the start with the 'pos0' pointer, and where the next '2' will go from the end with the 'pos2' pointer.
On every step of the loop we increment the current pointer 'i' or decrement the 'pos2' pointer, therefore only a single traversal of n steps is done, no more.

Time complexity: O(n)
Space complexity: O(1)
