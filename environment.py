import tsplib95
import numpy as np
import tspsolve

# Class representing the environment of the ant colony
"""
    rho: pheromone evaporation rate
"""
class Environment:
    def __init__(self, rho):
        self.rho = rho

        # Initialize the environment topology
        self.topology = tsplib95.load('att48-specs/att48.tsp')
        self.dimension = self.topology.dimension
        self.coordinates = list(self.topology.node_coords.values())

        # Initialize the pheromone map in the environment
        self.initialize_pheromone_map()

    def initialize_pheromone_map(self):
        self.pheromone_map = []
        value = self.dimension / self.c_n_n()
        self.pheromone_map = np.full((self.dimension, self.dimension), value)

    # Update the pheromone trails in the environment
    def update_pheromone_map(self, ants: list):
        self.trigger_pheromone_evaporation()

        for ant in ants:
            pheromone_updates = np.zeros_like(self.pheromone_map)
            for i, j in zip(ant.visited_locations[:-1], ant.visited_locations[1:]):
                added_pheromone = 1 / ant.travelled_distance
                pheromone_updates[i-1][j-1] += added_pheromone
                pheromone_updates[j-1][i-1] += added_pheromone
            self.pheromone_map += pheromone_updates


    def trigger_pheromone_evaporation(self):
        for i, row in enumerate(self.pheromone_map):
            for j, col in enumerate(row):
                self.pheromone_map[i][j] *= (1-self.rho)

    # Get the pheromone trails in the environment
    def get_pheromone_map(self):
        return self.pheromone_map

    def get_distance(self, i, j):
        return self.topology.get_weight(i, j)
    
    # Get the environment topology
    def get_possible_locations(self):
        return list(self.topology.get_nodes())

    def c_n_n(self):
        cost_matrix = np.array([
            [self.get_distance(i, j) for i in range(1, self.dimension + 1)]
            for j in range(1, self.dimension + 1)
        ])
        path = tspsolve.nearest_neighbor(cost_matrix)
        total_cost = np.sum([
            cost_matrix[path[i - 1], path[i]] for i in range(self.dimension)
        ])
        return total_cost


if __name__ == '__main__':
    environment = Environment(0.1)
