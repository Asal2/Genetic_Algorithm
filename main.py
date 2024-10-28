from GeneticGraphMiner import GeneticGraphMiner
from ReadGraph import print_connected_nodes
from ReadGraph import read_graph
from subgraph import generate_multiple_subgraphs
from PlotGraph import visualize_graph


def main():
    filename = 'hw3_cost239.txt'
    G = read_graph(filename)

    print_connected_nodes(G)

    generated_subgraphs = generate_multiple_subgraphs(G, num_subgraphs=100)

    print("this is generated subgraphs: ")
    print(generated_subgraphs)

    target_nodes = [1, 2, 8, 13]

    genetic_miner = GeneticGraphMiner(graph=G.edges(), target_nodes=target_nodes, population_size=100, generations=500)

    best_subgraph = genetic_miner.evolve()

    print("Best subgraph found:", best_subgraph)

    visualize_graph(graph=G, M=target_nodes, solution=best_subgraph)


if __name__ == "__main__":
    main()
