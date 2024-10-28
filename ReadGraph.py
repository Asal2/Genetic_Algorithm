from networkx import Graph


def read_graph(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        for line in file:
            if '//' in line:
                edge_info = line.split('//')[0].strip()
                if edge_info:
                    u, v = map(int, edge_info.split())
                    graph.add_edge(u, v)
    return graph


def print_connected_nodes(G):
    print("Connected nodes (edges):")
    for u, v in G.edges():
        print(f"Node {u} is connected to Node {v}")
