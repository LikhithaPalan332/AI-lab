from collections import deque

def bfs_shortest_path(graph, start, end, max_depth=4):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        current_node, path = queue.popleft()

        if len(path) - 1 > max_depth:
            continue

        if current_node == end:
            return path

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['F'],
    'F': ['H'],
    'G': [],
    'H': ['I','J'],
    'I': [],
    'J': ['K'],
    'K': ['L'],
    'L': []
}

start_node = 'A'
end_node = 'H'
max_depth_limit = 4

print(f"Searching for shortest path from {start_node} to {end_node} within {max_depth_limit} levels...")
path = bfs_shortest_path(graph, start_node, end_node, max_depth=max_depth_limit)

if path:
    print(f"Shortest path found: {path}")
    print(f"Path length: {len(path) - 1} levels")
else:
    print(f"No path found from {start_node} to {end_node} within {max_depth_limit} levels.")

print("\n--- Another Example (longer path) ---")
end_node_2 = 'G'
path_2 = bfs_shortest_path(graph, start_node, end_node_2, max_depth=max_depth_limit)
if path_2:
    print(f"Shortest path from {start_node} to {end_node_2}: {path_2}")
    print(f"Path length: {len(path_2) - 1} levels")
else:
    print(f"No path found from {start_node} to {end_node_2} within {max_depth_limit} levels.")

print("\n--- Example (path exceeding depth limit) ---")
graph_long = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D'],
    'D': ['E'],
    'E': ['F']
}
start_node_long = 'A'
end_node_long = 'F'
max_depth_limit_long = 3

print(f"Searching for shortest path from {start_node_long} to {end_node_long} within {max_depth_limit_long} levels...")
path_long = bfs_shortest_path(graph_long, start_node_long, end_node_long, max_depth=max_depth_limit_long)

if path_long:
    print(f"Shortest path found: {path_long}")
    print(f"Path length: {len(path_long) - 1} levels")
else:
    print(f"No path found from {start_node_long} to {end_node_long} within {max_depth_limit_long} levels.")
