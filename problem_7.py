class RouteTrieNode:
    """
    The RouteTrieNode stores a handler and a part of the route.
    """
    def __init__(self):
        self.part = None
        self.handler = None
        self.children = {}

    def insert(self, part):
        """
        Insert a route part as a child node for the current node.

        Args:
            part(string): A part of the route.
        Returns:
            None
        """
        self.children[part] = RouteTrieNode()


class RouteTrie:
    """
    The RouteTrie can store a route collection and retrieve a handler per route.
    """
    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, route_parts, handler):
        """
        Insert a route and a correspondig handler.

        Args:
            route_parts(list): A list containing the parts of the route.
            handler(string): A string representing the handler for the route.
        Returns:
            None
        """
        curr = self.root
        for part in route_parts:
            if part not in curr.children:
                curr.insert(part)
            curr = curr.children[part]
        curr.handler = handler

    def find(self, route_parts):
        """
        Find a route and returns the handler if exists.

        Args:
            route_parts(list): A list containing the parts of the route.
        Returns:
            (string): A string representing the handler for the route.
        """
        curr = self.root
        for part in route_parts:
            if part not in curr.children:
                return None
            curr = curr.children[part]
        return curr.handler


class Router:
    """
    The Router class uses the RouteTrie to store routes and handlers for later retrieval.
    A root handler and not found handler can be defined in constructor.
    """
    def __init__(self, root_handler, not_found_handler):
        self.routeTrie = RouteTrie()
        self.root_handler = root_handler
        self.not_found_handler = not_found_handler

    def add_handler(self, route, handler):
        """
        Adds a route with format 'root/home/path', and a corresponding handler.

        Args:
            route(string): A route path with '/' separator.
            handler(string): A string representing the handler for the route.
        Returns:
            None
        """
        route_parts = self.split_path(route)
        if len(route_parts) == 0:
            return
        self.routeTrie.insert(route_parts, handler)

    def lookup(self, route):
        """
        Search a route path in the RouteTrie and returns the corresponding handler, if exists.

        Args:
            route(string): A route path with '/' separator.
        Returns:
            (string): A string representing the handler for the route.
        """
        route_parts = self.split_path(route)
        if len(route_parts) == 0:
            return self.root_handler
        handler = self.routeTrie.find(route_parts)
        if handler is None:
            return self.not_found_handler
        return handler

    def split_path(self, path):
        """
        Separates the route path by '/' as separator, and removes trailing empty parts.

        Args:
            path(string): A route path with '/' separator.
        Returns:
            (list): A list containing the parts of the route.
        """
        if len(path) > 0 and path[0] == '/':
            path = path[1:]
        if len(path) > 0 and path[-1] == '/':
            path = path[0:-1]
        if len(path) == 0:
            return []
        return path.split('/')


def create_test_router():
    test_router = Router("root handler", "not found handler")
    test_router.add_handler("/home/about", "about handler")
    return test_router


def test_function(test_case):
    test_router = create_test_router()
    test_input, test_expected = test_case
    test_actual = test_router.lookup(test_input)
    if test_actual == test_expected:
        print("Pass")
    else:
        print("Fail")


test_function(('', 'root handler'))
test_function(('/', 'root handler'))
test_function(('//', 'root handler'))
test_function(('/zzz', 'not found handler'))
test_function(('xx/zz', 'not found handler'))
test_function(('/home', 'not found handler'))
test_function(('/home/', 'not found handler'))
test_function(('home/about', 'about handler'))
test_function(('home/about/', 'about handler'))
test_function(('/home/about', 'about handler'))
test_function(('/home/about/', 'about handler'))
test_function(('/home/about/me', 'not found handler'))
test_function(('/home/about/me/', 'not found handler'))
