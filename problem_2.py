import os
from collections import deque

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

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
    directories = deque()
    if os.path.isdir(path):
        directories.appendleft(path)
    while directories:
        directory = directories.pop()
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                if item_path.endswith(suffix):
                    found_files.append(item_path)
            elif os.path.isdir(item_path):
                directories.appendleft(item_path)
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
