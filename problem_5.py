class TrieNode:
    """
    A trie node with insert and suffixes methods.
    """
    def __init__(self):
        self.word_end = False
        self.children = {}

    def insert(self, char):
        """
        Insert a character as a child node for the current node.

        Args:
            char(string): Next character to insert as a child node.
        Returns:
            None
        """
        self.children[char] = TrieNode()

    def suffixes(self, suffix = ''):
        """
        Get all the suffixes starting from the current node.

        Args:
            suffix(string): A variable to collect all the suffixes on recursion.
        Returns:
            (array): A list containing all the suffixes.
        """
        res = []
        if self.word_end and suffix:
            res.append(suffix)
        for char, node in self.children.items():
            res += node.suffixes(suffix + char)
        return res


class Trie:
    """
    A Trie data structure with insert, find, and suffixes methods.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the Trie for later retrieval.

        Args:
        word(string): A word to be inserted
        Returns:
            (None)
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.insert(char)
            curr = curr.children[char]
        curr.word_end = True

    def find(self, prefix):
        """
        Find a prefix of a word and returns the intermediate trie node.

        Args:
            prefix(string): 
        Returns:
            (TrieNode): The intermediate trie node.
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return None
            curr = curr.children[char]
        return curr


def create_test_trie():
    test_trie = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym", 
        "fun", "function", "factory", 
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in wordList:
        test_trie.insert(word)
    return test_trie


def test_function(test_case):
    test_trie = create_test_trie()
    test_input, test_expected = test_case
    prefixNode = test_trie.find(test_input)
    test_actual = prefixNode.suffixes() if prefixNode else []
    if sorted(test_actual) == sorted(test_expected):
        print("Pass")
    else:
        print("Fail")


test_function(('', ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']))
test_function(('z', []))
test_function(('ant', ['hology', 'agonist', 'onym']))
test_function(('fu', ['n', 'nction']))
test_function(('tri', ['e', 'gger', 'gonometry', 'pod']))
test_function(('factory', []))
