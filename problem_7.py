class RouteTrieNode:
    def __init__(self):
        self.part = None
        self.handler = None
        self.children = {}

    def insert(self, part):
        self.children[part] = RouteTrieNode()


class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, route_parts, handler):
        curr = self.root
        for part in route_parts:
            if part not in curr.children:
                curr.insert(part)
            curr = curr.children[part]
        curr.handler = handler

    def find(self, route_parts):
        curr = self.root
        for part in route_parts:
            if part not in curr.children:
                return None
            curr = curr.children[part]
        return curr.handler


class Router:
    def __init__(self, root_handler, not_found_handler):
        self.routeTrie = RouteTrie()
        self.root_handler = root_handler
        self.not_found_handler = not_found_handler

    def add_handler(self, route, handler):
        route_parts = self.split_path(route)
        if len(route_parts) == 0:
            return
        self.routeTrie.insert(route_parts, handler)

    def lookup(self, route):
        route_parts = self.split_path(route)
        if len(route_parts) == 0:
            return self.root_handler
        handler = self.routeTrie.find(route_parts)
        if handler is None:
            return self.not_found_handler
        return handler

    def split_path(self, path):
        if len(path) > 0 and path[0] == '/':
            path = path[1:]
        if len(path) > 0 and path[-1] == '/':
            path = path[0:-1]
        if len(path) == 0:
            return []
        return path.split('/')


def test_function(test_case):
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    output = router.lookup(test_case[0])
    solution = test_case[1]
    if output == solution:
        print("Pass")
    else:
        print("Fail")


test_function(['', 'root handler'])
test_function(['/', 'root handler'])
test_function(['/home', 'not found handler'])
test_function(['/home/about', 'about handler'])
test_function(['/home/about/', 'about handler'])
test_function(['/home/about/me', 'not found handler'])
