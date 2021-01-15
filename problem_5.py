class TrieNode:
    def __init__(self):
        self.word_end = False
        self.children = {}
    
    def insert(self, char):
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        res = []
        if self.word_end:
            res.append(suffix)
        for char, node in self.children.items():
            res += node.suffixes(suffix + char)
        return res


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.insert(char)
            curr = curr.children[char]
        curr.word_end = True

    def find(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return None
            curr = curr.children[char]
        return curr


def test_function(test_case):
    MyTrie = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym", 
        "fun", "function", "factory", 
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in wordList:
        MyTrie.insert(word)
    prefixNode = MyTrie.find(test_case[0])
    output = set(prefixNode.suffixes())
    solution = set(test_case[1])
    if output == solution:
        print("Pass")
    else:
        print("Fail")


test_function(['tri', ['e', 'gger', 'gonometry', 'pod']])
