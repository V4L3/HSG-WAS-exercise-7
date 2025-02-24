import random
import numpy as np

from environment import Environment
from ant import Ant 

# Class representing the ant colony
"""
    ant_population: the number of ants in the ant colony
    iterations: the number of iterations 
    alpha: a parameter controlling the influence of the amount of pheromone during ants' path selection process
    beta: a parameter controlling the influence of the distance to the next node during ants' path selection process
    rho: pheromone evaporation rate
"""
class AntColony:
    def __init__(self, ant_population: int, iterations: int, alpha: float, beta: float, rho: float):
        self.ant_population = ant_population
        self.iterations = iterations
        self.alpha = alpha
        self.beta = beta
        self.rho = rho 

        # Initialize the environment of the ant colony
        self.environment = Environment(self.rho)

        # Initilize the list of ants of the ant colony
        self.ants = []

        # Initialize the ants of the ant colony
        for i in range(ant_population):
            
            # Initialize an ant on a random initial location 
            ant = Ant(self.alpha, self.beta, i+1)

            # Position the ant in the environment of the ant colony so that it can move around
            ant.join(self.environment)
        
            # Add the ant to the ant colony
            self.ants.append(ant)

    # Solve the ant colony optimization problem  
    def solve(self):
        shortest_distance = np.inf
        best_path = []

        for i in range(self.iterations):
            print("Iteration: " + str(i))
            local_shortest_path = np.inf
            for j, ant in enumerate(self.ants):
                ant.run()

                if ant.travelled_distance < local_shortest_path:
                    local_shortest_path = ant.travelled_distance

                if ant.travelled_distance < shortest_distance:
                    shortest_distance = ant.travelled_distance
                    best_path = ant.visited_locations

            print("Shortest path length: " + str(local_shortest_path))

            self.environment.update_pheromone_map(self.ants)

            if i != self.iterations - 1:
                for ant in self.ants:
                    ant.reset()


        return best_path, shortest_distance


def main():
    # Intialize the ant colony
    ant_colony = AntColony(48, 50, 1.0, 2.0, 0.5)

    # Solve the ant colony optimization problem
    solution, distance = ant_colony.solve()
    print("Solution: ", solution)
    print("Distance: ", distance)


if __name__ == '__main__':
    main()    