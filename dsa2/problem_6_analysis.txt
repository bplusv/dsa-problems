The 'find_files' function is implemented using a queue.
A straightforward recursive version was considered, but it may cause a stack overflow with very nested directories.
Also, a stack version was considered, but extra work needs to be done to keep track of already visited items.

The time complexity is O(n) relative to the number of items.
Space complexity is one level of the directory tree at a time. If there's a single directory with many single subdirectories at the same level, the space complexity may be O(n).
The queue version is expected to remove function call overhead, and prevent a call stack overflow, as python's default is just 1000.
Implemented a Queue class for practice, we could use python collections.deque class as well.
