class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = set() # set for O(1) membership test
        self.users = set()

    def add_group(self, group):
        self.groups.add(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


class Queue:
    class QueueNode:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.count = 0
        self.front = None
        self.back = None

    def size(self):
        return self.count

    def enqueue(self, value):
        new_node = self.QueueNode(value)
        if self.back:
            self.back.next = new_node
        self.back = new_node
        if not self.front:
            self.front = new_node
        self.count += 1

    def dequeue(self):
        assert self.count > 0, 'Queue is empty'
        value = self.front.value
        self.front = self.front.next
        self.count -= 1
        return value


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    queue = Queue()
    queue.enqueue(group)
    visited = {group} # add visited set to prevent loops
    while queue.size() > 0:
        curr_group = queue.dequeue()
        if user in curr_group.users:
            return True
        for sub_group in curr_group.groups:
            if sub_group not in visited:
                visited.add(sub_group)
                queue.enqueue(sub_group)
    return False


def test_case_1():
    company_group = Group('Company')
    company_group.add_user('my_user')
    print(is_user_in_group('my_user', company_group))

def test_case_2():
    company_group = Group('Company')
    commercial_group = Group('Commercial')
    healthcare_group = Group('Healthcare')
    healthcare_group.add_user('my_user')
    commercial_group.add_group(company_group) #loop
    commercial_group.add_group(healthcare_group)
    company_group.add_group(commercial_group)
    print(is_user_in_group('my_user', company_group))

def test_case_3():
    company_group = Group('Company')
    company_group.add_user('user1')
    commercial_group = Group('Commercial')
    commercial_group.add_user('user2')
    healthcare_group = Group('Healthcare')
    healthcare_group.add_user('user3')
    commercial_group.add_group(healthcare_group)
    company_group.add_group(commercial_group)
    development_group = Group('Development')
    development_group.add_user('user4')
    company_group.add_group(development_group)
    print(is_user_in_group('my_user', company_group))


test_case_1()
# True

test_case_2()
# True

test_case_3()
# False


