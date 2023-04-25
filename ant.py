import random

# Class representing an artificial ant of the ant colony
"""
    alpha: a parameter controlling the influence of the amount of pheromone during ants' path selection process
    beta: a parameter controlling the influence of the distance to the next node during ants' path selection process
"""
class Ant:
    def __init__(self, alpha: float, beta: float, initial_location: int):
        self.alpha = alpha
        self.beta = beta
        self.initial_location = initial_location
        self.current_location = initial_location
        self.travelled_distance = 0
        self.visited_locations = [initial_location]

    # The ant runs to visit all the possible locations of the environment 
    def run(self):
        for i in range(len(self.environment.get_possible_locations()) - 1):
            next_location = self.select_path()
            self.travelled_distance += self.environment.get_distance(self.current_location, next_location)
            self.current_location = next_location
            self.visited_locations.append(next_location)

        # Add distance back to the starting location
        self.travelled_distance += self.environment.get_distance(self.current_location, self.visited_locations[0])


    # Select the next path based on the random proportional rule of the ACO algorithm
    def select_path(self):
        locations = []
        probabilities = []
        divisor = 0

        # Create a list of all possible unvisited locations
        possible_locations = list(set(self.environment.get_possible_locations()) - set(self.visited_locations))

        # Calculate probability for each location
        for location in possible_locations:
            tau = self.environment.pheromone_map[self.current_location - 1][location - 1]
            eta = 1 / self.environment.get_distance(self.current_location, location)
            value = (tau ** self.alpha) * (eta ** self.beta)
            locations.append(location)
            probabilities.append(value)
            divisor += value

        # Normalize probabilities
        if divisor > 0.0:
            probabilities = [prob / divisor for prob in probabilities]
        else:
            probabilities = [1 / len(probabilities)] * len(probabilities)

        # Select a location based on probabilities
        return random.choices(locations, probabilities)[0]

    # Position an ant in an environment
    def join(self, environment):
        self.environment = environment

    def reset(self):
        self.current_location = self.initial_location
        self.visited_locations = [self.current_location]
        self.travelled_distance = 0
