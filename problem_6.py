class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedSet:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = "linked_set: "
        if not cur_head:
            out_string += "<empty> "
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        prev = None
        curr = self.head
        while curr:
            if new_node.value == curr.value:
                return
            if new_node.value < curr.value:
                new_node.next = curr
                if not prev:
                    self.head = new_node
                else:
                    prev.next = new_node
                return
            prev = curr
            curr = curr.next
        prev.next = new_node

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size


def union(llist_1, llist_2):
    result = LinkedSet()
    l = llist_1.head
    r = llist_2.head
    while l and r:
        if l.value < r.value:
            result.append(l.value)
            l = l.next
        elif r.value < l.value:
            result.append(r.value)
            r = r.next
        else:
            result.append(l.value)
            l = l.next
            r = r.next
    while l:
        result.append(l.value)
        l = l.next
    while r:
        result.append(r.value)
        r = r.next
    return result

def intersection(llist_1, llist_2):
    result = LinkedSet()
    l = llist_1.head
    r = llist_2.head
    while l and r:
        if l.value < r.value:
            l = l.next
        elif r.value < l.value:
            r = r.next
        else:
            result.append(l.value)
            l = l.next
            r = r.next
    return result
    

def test_case_1():
    print('--- test_case_1 ---')
    linked_list_1 = LinkedSet()
    linked_list_2 = LinkedSet()
    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]
    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)
    print (union(linked_list_1,linked_list_2))
    print (intersection(linked_list_1,linked_list_2))

def test_case_2():
    print('--- test_case_2 ---')
    # test empty intersection
    linked_list_1 = LinkedSet()
    linked_list_2 = LinkedSet()
    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]
    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)
    print (union(linked_list_1,linked_list_2))
    print (intersection(linked_list_1,linked_list_2))

def test_case_3():
    print('--- test_case_3 ---')
    # test empty set + single item set
    linked_list_1 = LinkedSet()
    linked_list_2 = LinkedSet()
    element_1 = []
    element_2 = [1]
    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)
    print (union(linked_list_1,linked_list_2))
    print (intersection(linked_list_1,linked_list_2))

def test_case_4():
    print('--- test_case_4 ---')
    # test empty sets
    linked_list_1 = LinkedSet()
    linked_list_2 = LinkedSet()
    element_1 = []
    element_2 = []
    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)
    print (union(linked_list_1,linked_list_2))
    print (intersection(linked_list_1,linked_list_2))

def test_case_5():
    print('--- test_case_5 ---')
    linked_list_1 = LinkedSet()
    linked_list_2 = LinkedSet()
    element_1 = [4,3,2,1,5,6]
    element_2 = [8,7,1,5,6]
    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)
    print (union(linked_list_1,linked_list_2))
    print (intersection(linked_list_1,linked_list_2))



test_case_1()
# linked_set: 1 -> 2 -> 3 -> 4 -> 6 -> 9 -> 11 -> 21 -> 32 -> 35 -> 65 ->
# linked_set: 4 -> 6 -> 21 ->

test_case_2()
# linked_set: 1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 35 -> 65 ->
# linked_set: <empty>

test_case_3()
# linked_set: 1 ->
# linked_set: <empty>

test_case_4()
# linked_set: <empty>
# linked_set: <empty>


test_case_5()
# linked_set: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 
# linked_set: 1 -> 5 -> 6 ->
