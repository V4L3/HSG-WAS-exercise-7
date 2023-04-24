import math
import tsplib95
import tspsolve
import numpy as np

# Class representing the environment of the ant colony
"""
    rho: pheromone evaporation rate
"""
class Environment:
    def __init__(self, rho):

        self.rho =rho
        self.evaporation_rate = 0.5
        
        # Initialize the environment topology
        self.topology = tsplib95.load('att48-specs/att48.tsp')
        self.G = self.topology.get_graph()
        # print(self.G.nodes[1]["coord"][0])
        # Intialize the pheromone map in the environment
        self.pheromone_map = self.initialize_pheromone_map()
        # self.update_pheromone_map()
        # print(self.pheromone_map)
        pass 

    # Intialize the pheromone trails in the environment
    def initialize_pheromone_map(self):
        print("init pheromone map")
        pheromone_map = []
        initial_pheromone_value = len(self.G.nodes) / self.c_n_n()
        num_nodes = 48
        for i in range(num_nodes):
            row = [initial_pheromone_value] * num_nodes
            pheromone_map.append(row)
        return pheromone_map

    # Update the pheromone trails in the environment
    def update_pheromone_map(self, ants):
        self.trigger_pheromone_evaporation()

        for ant in ants:
            for idx, node in enumerate(ant.visited_locations):
                new_pheromone_value = 1 / ant.travelled_distance
                if(idx >= 0):
                    i = ant.visited_locations[idx]
                    j = ant.visited_locations[46]
                else:
                    i = ant.visited_locations[idx-1]
                    j = ant.visited_locations[idx]
                self.pheromone_map[i-1][j-1] += new_pheromone_value
                self.pheromone_map[j-1][i-1] += new_pheromone_value

    # Trigger the pheromone evaporation
    def trigger_pheromone_evaporation(self):
        for i, row in enumerate(self.pheromone_map):
            for j, col in enumerate(row):
                self.pheromone_map[i][j] *= (1-self.rho)

    # Get the pheromone trails in the environment
    def get_pheromone_map(self):
        return self.pheromone_map
    
    # Get the environment topology
    def get_possible_locations(self):
        # print("reading locations")
        return self.G.nodes
    
    def c_n_n(self):
        num_nodes = 48
        cost_matrix = np.empty((num_nodes, num_nodes))
        for i in range(1, num_nodes + 1):
            for j in range(1, num_nodes + 1):
                cost_matrix[i-1][j-1] = self.topology.get_weight(i, j)

        path = tspsolve.nearest_neighbor(cost_matrix)

        total_cost = 0
        for i in range(1, len(path)):
            current_node = path[i]
            previous_node = path[i-1]
            total_cost += cost_matrix[previous_node, current_node]

        return total_cost
