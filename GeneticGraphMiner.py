import random

class GeneticGraphMiner:
    def __init__(self, graph, target_nodes, population_size=100, generations=500):
        self.graph = graph
        self.target_nodes = set(target_nodes)
        self.population_size = population_size
        self.generations = generations
        self.population = self.initialize_population()

    def initialize_population(self):
        # Create a random initial population of subgraphs with varying sizes
        population = []
        for _ in range(self.population_size):
            subgraph_size = random.randint(len(self.graph) // 4, len(self.graph) // 2)
            subgraph_edges = random.sample(list(self.graph), subgraph_size)
            population.append(subgraph_edges)
        return population

    def fitness(self, subgraph):
        # Extract nodes from the subgraph edges
        connected_nodes = set()
        for edge in subgraph:
            connected_nodes.update(edge)

        covered_target_nodes = len(self.target_nodes.intersection(connected_nodes))

        if covered_target_nodes == 0:
            return 0

        extra_nodes = len(connected_nodes - self.target_nodes)

        node_coverage_score = covered_target_nodes / len(self.target_nodes)
        edge_penalty = len(subgraph) / len(self.graph)
        node_penalty = extra_nodes / len(connected_nodes)

        fitness_score = node_coverage_score / (1 + edge_penalty + node_penalty)

        return fitness_score

    def crossover(self, parent1, parent2):
        # Combine edges from both parents to create a child subgraph
        midpoint = len(parent1) // 2
        child_edges = parent1[:midpoint] + parent2[midpoint:]
        return child_edges

    def mutate(self, subgraph):
        # Randomly add or remove an edge
        if random.random() < 0.5 and len(subgraph) > 1:
            subgraph.remove(random.choice(subgraph))
        else:
            new_edge = random.choice(list(self.graph))
            if new_edge not in subgraph:
                subgraph.append(new_edge)
        return subgraph

    def evolve(self):
        best_individual = None  # Initialize best_individual

        for generation in range(self.generations):
            fitnesses = [self.fitness(ind) for ind in self.population]

            average_fitness = sum(fitnesses) / len(fitnesses)
            print(f"Generation {generation}: Average fitness = {average_fitness * 100:.2f}%")

            if max(fitnesses) == 0:
                print(f"Generation {generation}: No valid subgraphs found.")
                continue

            best_individual = self.population[fitnesses.index(max(fitnesses))]

            sorted_population = [ind for _, ind in sorted(zip(fitnesses, self.population), reverse=True)]
            parents = sorted_population[:self.population_size // 2]

            new_population = parents[:]

            while len(new_population) < self.population_size:
                parent1 = random.choice(parents)
                parent2 = random.choice(parents)
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)

            self.population = new_population

            print(f"Generation {generation}: Best fitness = {max(fitnesses) * 100:.2f}%")
            print(f"Number of edges in the best subgraph: {len(best_individual)}")
            if max(fitnesses) == 1.0:
                break

        return best_individual
