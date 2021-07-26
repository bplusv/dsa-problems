import sys

class MinHeap:
    def __init__(self):
        self.arr = []

    def _sift_up(self, i):
        p = (i - 1) // 2
        while i > 0 and self.arr[i][0] < self.arr[p][0]:
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p
            p = (i - 1) // 2

    def _sift_down(self, i):
        n = len(self.arr)
        l, r = (i * 2) + 1, (i * 2) + 2
        while ((l < n and self.arr[i][0] > self.arr[l][0]) or 
               (r < n and self.arr[i][0] > self.arr[r][0])):
            mc = r if (r < n and self.arr[r][0] < self.arr[l][0]) else l
            self.arr[i], self.arr[mc] = self.arr[mc], self.arr[i]
            i = mc
            l, r = (i * 2) + 1, (i * 2) + 2

    def insert(self, key, value):
        self.arr.append((key, value))
        i = len(self.arr) - 1
        self._sift_up(i)
    
    def extract_min(self):
        assert len(self.arr) > 0, 'Heap is empty'
        key, value = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self._sift_down(0)
        return value

    def size(self):
        return len(self.arr)


class HuffmanNode:
    def __init__(self, freq=0, char=None):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

def get_huffman_code_table(root, path=''):
    if root.char is not None:
        return { root.char: path }
    l = get_huffman_code_table(root.left, path + '0')
    r = get_huffman_code_table(root.right, path + '1')
    c = l.copy()
    c.update(r)
    return c

def huffman_encoding(data):
    assert len(data) > 0, 'empty data'
    freq_dict = {}
    mheap = MinHeap()
    for c in data:
        freq_dict[c] = freq_dict.get(c, 0) + 1
    for c, freq in freq_dict.items():
        node = HuffmanNode(freq, c)
        mheap.insert(freq, node)
    while mheap.size() > 1:
        new_node = HuffmanNode()
        new_node.left = mheap.extract_min()
        new_node.right = mheap.extract_min()
        new_node.freq = new_node.left.freq + new_node.right.freq
        mheap.insert(new_node.freq, new_node)
    huffman_tree = mheap.extract_min()
    # If there's only one symbol in huffman tree, return symbol total count in binary
    if huffman_tree.left is None:
        return '{0:b}'.format(len(data)), huffman_tree
    code_table = get_huffman_code_table(huffman_tree)
    encoded_data = ''
    for c in data:
        encoded_data += code_table[c]
    return encoded_data, huffman_tree


def huffman_decoding(data, tree):
    decoded_data = ''
    # If there's only one symbol in huffman tree, repeat symbol count times
    if tree.left is None:
        return tree.char * int(data, base=2)
    curr = tree
    for c in data:
        if c == '0':
            curr = curr.left
        elif c == '1':
            curr = curr.right
        if curr.char is not None:
            decoded_data += curr.char
            curr = tree
    return decoded_data


def test_case_1():
    # One symbol repetition
    data = 'zzzzzzzz'
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert data == decoded_data
    print('original: {}, compressed: {}'.format(sys.getsizeof(data), sys.getsizeof(int(encoded_data, base=2))))

def test_case_2():
    # High repetition example, 1/10 compression
    data = 'a' * 10000 + 'c'
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert data == decoded_data
    print('original: {}, compressed: {}'.format(sys.getsizeof(data), sys.getsizeof(int(encoded_data, base=2))))

def test_case_3():
    # one symbol, one time
    data = 'x'
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert data == decoded_data
    print('original: {}, compressed: {}'.format(sys.getsizeof(data), sys.getsizeof(int(encoded_data, base=2))))


if __name__ == "__main__":
    a_great_sentence = "The bird is the word"
    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    test_case_1()
    # original: 57, compressed: 28

    test_case_2()
    # original: 10050, compressed: 1360

    test_case_3()
    # original: 50, compressed: 28
