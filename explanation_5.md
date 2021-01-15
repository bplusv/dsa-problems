The Trie data structure problem has 3 main operations: insert, find, suffixes.
For the insert operation, a word is provided and, in the worst case all the nodes for each word character must be created, taking linear time O(n) where n is the word length.,
For the find operation, the word is provided and the Trie is traversed in O(n) where n is the word length.
For the suffixes operation, a depth-first recursive approach is used traversing the whole Sub-Trie from the starting TrieNode, this takes O(n) time, where n is the size of the whole Sub-Trie. In the worst case, a linear Trie will use O(n) space, due to the stack recursion.


Insert Time Complexity: O(n)
Insert Space Complexity: O(1)

Find Time Complexity: O(n)
Find Space Complexity: O(1)

Suffixes Time Complexity: O(n)
Suffixes Space Complexity: O(n)
