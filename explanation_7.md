The Trie based HTTPRouter is implemented with a simple trie data structure. Instead of adding a TrieNode per character, this structure adds a node per path part. This prevents a very large Trie and simplifies the traversal.

The insert and find time complexity is linear to the input size of the parts list. The space complexity for the Trie methods uses constant space. The Trie class itself reserves space outside the method calls.

RouteTrie Insert Time Complexity: O(n)
RouteTrie Insert Space Complexity: O(1)

RouteTrie Find Time Complexity: O(n)
RouteTrie Find Space Complexity: O(1)
