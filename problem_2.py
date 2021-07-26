import os

class Queue:
    """ A regular Queue class with FIFO behavior 
        with enqueue and dequeue methods.
    """
    class QueueNode:
        """ Internal class for Queue node """
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.front = None
        self.back = None
        self._size = 0

    def size(self):
        return self._size
    
    def enqueue(self, value):
        node = self.QueueNode(value)
        if self.back:
            self.back.next = node
        self.back = node
        if not self.front:
            self.front = node
        self._size += 1

    def dequeue(self):
        assert self._size > 0, 'Queue is empty'
        node = self.front
        self.front = self.front.next
        if not self.front:
            self.back = None
        self._size -= 1
        return node.value


def find_files(suffix, path):
    """ Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """
    found_files = []
    directories = Queue()
    if os.path.isdir(path):
        directories.enqueue(path)
    while directories.size() > 0:
        directory = directories.dequeue()
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                if item_path.endswith(suffix):
                    found_files.append(item_path)
            elif os.path.isdir(item_path):
                directories.enqueue(item_path)
    return found_files


def test_case_1():
    output = find_files('.c', 'testdir')
    print(output)

def test_case_2():
    output = find_files('.h', 'testdir')
    print(output)

def test_case_3():
    output = find_files('.py', 'testdir')
    print(output)


test_case_1()
# ['testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c', 'testdir/subdir3/subsubdir1/b.c']

test_case_2()
# ['testdir/t1.h', 'testdir/subdir5/a.h', 'testdir/subdir1/a.h', 'testdir/subdir3/subsubdir1/b.h']

test_case_3()
# []
