class Node:
    def __init__(self, state, parent=None, cost=0, function=None):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.function = function

    def is_root(self):
        return self.parent == None

    def is_repeated(self, max_depth=6):
        if self.is_root():
            return False

        current_node = self.parent

        while max_depth > 0:
            if current_node.state == self.state:
                return True

            if current_node.is_root():
                return False

            current_node = current_node.parent
            max_depth -= 1

        return False

    def path_to_root(self):
        if (self.is_root()):
            return [self]

        return self.parent.path_to_root() + [self]


def bfs(state, functions, objective):
    start_node = Node(state)

    queue = [start_node]

    solution = node_bfs(queue, functions, objective)

    return (solution.path_to_root(), solution.cost) if solution != None else None


def node_bfs(queue, functions, objective):
    if not queue:
        return None

    current_node = queue.pop(0)

    if objective(*(current_node.state)):
        return current_node

    for function in functions:
        call = function(*(current_node.state))

        function_name = function.__name__

        if call != False:
            child = Node(call, current_node, current_node.cost +
                         1, function=function_name)

            if not child.is_repeated():
                queue.append(child)

    return node_bfs(queue, functions, objective)


def dfs(state, functions, objective, max_cost):
    start_node = Node(state)

    queue = [start_node]

    solution = node_dfs(queue, functions, objective, max_cost, None)

    return (solution.path_to_root(), solution.cost) if solution != None else None


def node_dfs(stack, functions, objective, max_cost, best_node):
    # Implementation using a stack https://en.wikipedia.org/wiki/Depth-first_search DFS iterative
    if not stack:
        return best_node

    current_node = stack.pop()

    if current_node.cost > max_cost:
        return node_dfs(stack, functions, objective, max_cost, best_node)

    if objective(*(current_node.state)):
        if best_node == None or best_node.cost < max_cost:
            best_node = current_node
            max_cost = current_node.cost

        return node_dfs(stack, functions, objective, max_cost, best_node)

    for function in functions:
        call = function(*(current_node.state))

        function_name = function.__name__

        if call != False:
            child = Node(call, current_node, current_node.cost +
                         1, function=function_name)

            if not child.is_repeated():
                stack.append(child)

    return node_dfs(stack, functions, objective, max_cost, best_node)


def iterative_deepening(state, functions, objective, max_depth):
    current_depth = 0
    result = None

    while max_depth > current_depth and result == None:
        result = dfs(state, functions, objective, current_depth)
        current_depth += 1

    return result


def ex1_pretty_print_path(path):
    path = list(map(lambda node:
                    (f"then {node.function} and get " if node.parent else "") + f"({node.state[0]}, {node.state[1]})", path))

    print(" ".join(path))
