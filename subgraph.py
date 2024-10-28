import random


def random_connected_subgraph(G, num_nodes):
    # Pick a random starting node
    start_node = random.choice(list(G.nodes()))

    subgraph_nodes = {start_node}

    # Keep adding nodes until we have the desired number of nodes
    while len(subgraph_nodes) < num_nodes:
        neighbors = set()
        for node in subgraph_nodes:
            neighbors.update(set(G.neighbors(node)))

        neighbors -= subgraph_nodes

        if not neighbors:
            break

        new_node = random.choice(list(neighbors))
        subgraph_nodes.add(new_node)

    subgraph = G.subgraph(subgraph_nodes).copy()

    cost = subgraph.size()
    print('this is subgraph size:', cost)

    return subgraph, cost


# Function to generate 100 random connected subgraphs with direct links
def generate_multiple_subgraphs(G, num_subgraphs=100):
    total_nodes = len(G.nodes())

    subgraphs = []

    for _ in range(num_subgraphs):
        num_nodes = random.randint(3, total_nodes)

        subgraph, Link = random_connected_subgraph(G, num_nodes)

        subgraphs.append((subgraph, Link))

        print(f"Subgraph {_ + 1}:")
        print(f"Nodes: {list(subgraph.nodes())}")
        print(f"Edges: {list(subgraph.edges())}")
        print(f"Link: {Link}\n")

    return subgraphs
