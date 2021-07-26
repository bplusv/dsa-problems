For the Trie insert operation worst case, all the nodes for each word character must be created, taking linear time O(n) where n is the word length.
For the Trie find operation the Trie is traversed in O(n) where n is the word length.
For the TrieNode suffixes operation, a depth-first recursive function is used to traverse the whole sub trie, from the starting node. This takes O(n) time, where n is the size of the whole sub trie. In the worst case, the suffixes operation will use O(n) space, due to the stack recursion.

Insert Time Complexity: O(n)
Insert Space Complexity: O(1)

Find Time Complexity: O(n)
Find Space Complexity: O(1)

Suffixes Time Complexity: O(n)
Suffixes Space Complexity: O(n)
