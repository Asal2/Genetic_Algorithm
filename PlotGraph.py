import matplotlib.pyplot as plt
import networkx as nx


def visualize_graph(graph, M, solution):
    G = graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    nx.draw_networkx_edges(G, pos, edgelist=solution, edge_color='red', width=2)
    nx.draw_networkx_nodes(G, pos, nodelist=M, node_color='yellow', node_size=500, label='Target Nodes')

    plt.legend()
    plt.show()
