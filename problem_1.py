class LRU_Cache:
    class QueueNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self, capacity=5):
        assert capacity > 0, 'capacity should be greater than zero'
        self.capacity = capacity
        self.node_dict = {}
        self.queue_back = None
        self.queue_front = None

    def _remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.queue_back = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.queue_front = node.prev
        node.prev = node.next = None

    def _enqueue_node(self, node):
        node.next = self.queue_back
        if self.queue_back:
            self.queue_back.prev = node
        self.queue_back = node
        if not self.queue_front:
            self.queue_front = node

    def _dequeue_node(self):
        old_node = self.queue_front
        self._remove_node(self.queue_front)
        return old_node

    def size(self):
        return len(self.node_dict)

    def get(self, key):
        if key in self.node_dict:
            node = self.node_dict[key]
            self._remove_node(node)
            self._enqueue_node(node)
            return node.value
        return -1

    def set(self, key, value):
        if key in self.node_dict:
            node = self.node_dict[key]
            node.value = value
            self._remove_node(node)
            self._enqueue_node(node)
        else:
            node = self.QueueNode(key, value)
            if len(self.node_dict) == self.capacity:
                old_node = self._dequeue_node()
                del self.node_dict[old_node.key]
            self.node_dict[key] = node
            self._enqueue_node(node)
    
    def __repr__(self):
        out = 'dict: {' + ', '.join(f'{k}:{n.value}' for k,n in self.node_dict.items()) + '}\n'
        out += 'queue: '
        curr = self.queue_back
        while curr:
            out += f'({curr.key}, {curr.value})'
            if curr.next:
                out += ' -> '
            curr = curr.next
        return out


def test_case_1():
    output = []
    my_cache = LRU_Cache(5)
    my_cache.set(1, 1)
    my_cache.set(2, 2)
    my_cache.set(3, 3)
    my_cache.set(4, 4)
    output.append(my_cache.get(1))
    output.append(my_cache.get(2))
    output.append(my_cache.get(9))
    my_cache.set(5, 5)
    my_cache.set(6, 6)
    output.append(my_cache.get(3))
    print(output)

def test_case_2():
    output = []
    try:
        my_cache = LRU_Cache(0)
    except Exception as e:
        output.append(str(e))
    print(output)

def test_case_3():
    output = []
    my_cache = LRU_Cache(100)
    for i in range(1, 101):
        my_cache.set(i, i)
    output.append(my_cache.get(1))
    my_cache.set(101, 101)
    output.append(my_cache.get(2))
    output.append(my_cache.get(3))
    my_cache.set(102, 102)
    output.append(my_cache.get(4))
    print(output)


test_case_1()
# [1, 2, -1, -1]

test_case_2()
# ['capacity shoud be greater than zero']

test_case_3()
# [1, -1, 3, -1]
