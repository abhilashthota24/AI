class Graph:
    graph = {}

    @staticmethod
    def add_edge(u, v):
        if u not in Graph.graph:
            Graph.graph[u] = []
        Graph.graph[u].append(v)

    @staticmethod
    def depth_limited_dfs(current, target, depth_limit, depth=0, path=None):
        if path is None:
            path = []

        path.append(current)

        if depth > depth_limit:
            path.pop()
            return False, []

        if current == target:
            return True, path

        if current not in Graph.graph:
            path.pop()
            return False, []

        for neighbor in Graph.graph[current]:
            found, result_path = Graph.depth_limited_dfs(neighbor, target, depth_limit, depth + 1, path)
            if found:
                return True, result_path

        path.pop()
        return False, []

edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'F'), ('C', 'E'), ('D', 'E'), ('D', 'F'), ('F', 'E')]
for u, v in edges:
    Graph.add_edge(u, v)

source = 'A'
depth_limit = 1

print(f"Exploring all nodes from '{source}' within depth limit {depth_limit}:")
for node in Graph.graph:
    if node != source:
        found, path = Graph.depth_limited_dfs(source, node, depth_limit)
        print(f"Path to {node}: {' -> '.join(path)}" if found else f"No valid path to {node} within depth limit {depth_limit}")
