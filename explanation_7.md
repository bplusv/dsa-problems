The Trie-based HTTP Router is implemented with a simple trie data structure. Instead of adding a Trie Node per character, this structure adds a node per path part. This prevents a very large Trie, and simplifies traversal. The insert and find time complexity is linear to the input size "array_parts". The space complexity for the Trie in the worst case, where all the paths are unique is linear to the "array_parts".

RouteTrie Insert Time Complexity: O(n)
RouteTrie Insert Space Complexity: O(n)

RouteTrie Find Time Complexity: O(n)
RouteTrie Find Space Complexity: O(n)