A Least Recently Used Cache (LRU Cache) is implemented using a doubly-linked list and a dictionary.
The dictionary is used to track the nodes on the linked list, without the need to traverse the list.
Also, a doubly-linked list was needed, to be able to remove the item using only one node reference.

The amortized time complexity is O(1).
For the 'get' operation, a lookup in the dictionary is used to retrieve value.
For the 'set' operation, a constant number of operations are performed to update the linked list, to set the recently accessed item to the back of the queue. If the max capacity is reached, the front of the queue is removed from the list and dictionary as well. The least recently used item is evicted from the cache first.
