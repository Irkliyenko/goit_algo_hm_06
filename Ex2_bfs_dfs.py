from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import timeit


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # Visit the vertex
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")  # Visit the vertex
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)


if __name__ == '__main__':
    graph = {
        'A': {'B': {'weight': 5}, 'C': {'weight': 8}},
        'B': {'D': {'weight': 10}},
        'C': {'E': {'weight': 7}},
        'D': {'F': {'weight': 15}},
        'E': {'F': {'weight': 12}},
        'F': {'G': {'weight': 8}},
        'G': {'H': {'weight': 6}},
        'H': {'I': {'weight': 9}},
        'I': {'J': {'weight': 11}},
        'J': {'K': {'weight': 5}},
        'K': {'L': {'weight': 7}},
        'L': {'M': {'weight': 8}},
        'M': {},  # Assuming 'M' doesn't have outgoing edges
    }

    G = nx.DiGraph(graph)
    # Measure BFS time
    bfs_time = timeit.timeit(
        lambda: bfs_recursive(graph, deque(['A'])), number=5)
    # Measure DFS time
    dfs_time = timeit.timeit(lambda: dfs_recursive(graph, 'A'), number=5)
    bfs_tree = nx.bfs_tree(G, 'A')
    dfs_tree = nx.dfs_tree(G, 'A')

    print(f"BFS time: {bfs_time}")
    print(f"DFS time: {dfs_time}")
    print("BFS Tree Nodes:", list(bfs_tree.nodes()))
    print("DFS Tree Nodes:", list(dfs_tree.nodes()))

    pos = nx.shell_layout(G)
    options = {
        'node_color': 'green',
        'node_size': 500,
        'edge_color': 'pink',
        'width': 2,
        'with_labels': True,
        'font_color': 'white',
        'font_size': 6.5,
        'font_weight': "bold"
    }

    nx.draw(G, pos, **options)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title('City Transport Network')
    plt.show()

    '''
    The difference between the BFS and DFS algorithms is that the DFS algorithm is going
    to explore as far as possible along each branch before backtracking, while the BFS algorithm
    expands the shallowest unexpanded node at each iteration, leading to the discovery of the
    shortest paths first. This can be observed in the BFS and DFS tree nodes printed above.

    Additionally, in this specific scenario DFS was faster than BFS. However the difference if not that big. 
    The actual performance can vary depending on the characteristics of the graph, the starting node, and other factors. 
    In general, BFS tends to be more efficient for finding shortest paths in unweighted graphs, while DFS might perform 
    better in certain scenarios or for specific types of graphs.
    '''
