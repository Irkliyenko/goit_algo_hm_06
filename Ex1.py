import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph for the city transport network
G = nx.DiGraph()
# Nodes representing locations in the city
locations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
# Edges representing reactions between locations
edges = [('A', 'B', {'weight': 5}),
         ('A', 'C', {'weight': 8}),
         ('B', 'D', {'weight': 10}),
         ('C', 'E', {'weight': 7}),
         ('D', 'F', {'weight': 15}),
         ('E', 'F', {'weight': 12}),
         ('F', 'G', {'weight': 8}),
         ('G', 'H', {'weight': 6}),
         ('H', 'I', {'weight': 9}),
         ('I', 'J', {'weight': 11}),
         ('J', 'K', {'weight': 5}),
         ('K', 'L', {'weight': 7}),
         ('L', 'M', {'weight': 8})]

# Add nodes and edges to the graph
G.add_nodes_from(locations)
G.add_edges_from(edges)

number_of_locations = G.number_of_nodes()
number_of_edges = G.number_of_edges()
degree_centrality = nx.degree_centrality(G)

print(
    f'Number of locations: {number_of_locations}, number of edges: {number_of_edges}, degree centrality: {degree_centrality}')

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

plt.title('City Transport Network')
plt.show()
