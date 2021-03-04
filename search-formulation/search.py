class Node:
    def __init__(self, state, parent=None, cost=0, function=None):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.function = function

    def is_root(self):
        return self.parent == None

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
            queue.append(
                Node(call, current_node, current_node.cost + 1, function=function_name))

    return node_bfs(queue, functions, objective)


def pretty_print_path(path):
    path = list(map(lambda node:
                    (f"then {node.function} and get " if node.parent else "") + f"({node.state[0]}, {node.state[1]})", path))

    print(" ".join(path))
