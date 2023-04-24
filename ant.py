
# Class representing an artificial ant of the ant colony
"""
    alpha: a parameter controlling the influence of the amount of pheromone during ants' path selection process
    beta: a parameter controlling the influence of the distance to the next node during ants' path selection process
"""
from math import sqrt


class Ant():
    def __init__(self, alpha: float, beta: float, initial_location):
        self.alpha = alpha
        self.beta = beta
        self.initial_location = initial_location
        self.current_location = initial_location
        self.travelled_distance = 0
        self.visited_locations = []
        # self.possible_locations = self.environment.get_possible_locations()

    # The ant runs to visit all the possible locations of the environment 
    def run(self):
        for i in range(47):
            available_cities = list(set(self.possible_locations).difference(set(self.visited_locations)))
            current_location = self.possible_locations[self.current_location]
            next_location = self.select_path(available_cities, current_location)
            # print("next_location: " + str(next_location))
            self.visited_locations.append(next_location)
            # print(str(self.possible_locations[self.current_location]))
            # print(str(self.possible_locations[next_location]))
            self.travelled_distance += self.get_distance(i=self.possible_locations[self.current_location], j=self.possible_locations[next_location])
            # print(self.travelled_distance)

    # Select the next path based on the random proportional rule of the ACO algorithm
    def select_path(self, available_cities, current_location):
        probabilities = []
        pheromone_map = self.environment.get_pheromone_map()
        denominator = 0.0
        
        # compute the denominator of the probability formula
        for location in available_cities:
            tau_ij = pheromone_map[self.current_location-1][location-1]
            eta_ij = self.get_distance(current_location, self.possible_locations[location])
            denominator += pow(tau_ij, self.alpha) * pow(eta_ij, self.beta)
        
        # compute the probability of each available city
        for location in available_cities:
            tau_ij = pheromone_map[self.current_location-1][location-1]
            eta_ij = self.get_distance(current_location, self.possible_locations[location])
            numerator = pow(tau_ij, self.alpha) * pow(eta_ij, self.beta)
            probability = numerator / denominator
            probabilities.append(probability)
        
        city_prob = list(zip(available_cities, probabilities))  # combine the two lists
        max_city = max(city_prob, key=lambda x: x[1])  # find the city with the highest probability

        # print("The city with the highest probability is:", max_city[0])

        return max_city[0]

    def get_distance(self,i,j):
        # print("i: "+str(i))
        # print("j: "+str(j))
        xd = i["coord"][0] - j["coord"][0]
        yd = i["coord"][1] - j["coord"][1]
        rij = sqrt((xd*xd + yd*yd) / 10.0)
        tij = round(rij)
        if (tij < rij):
            dij = tij + 1
        else:
            dij = tij
        
        return dij
    
    def reset(self):
        self.current_location = self.initial_location
        self.travelled_distance = 0
        self.visited_locations = []
        self.possible_locations = self.environment.get_possible_locations()
        # print(self.possible_locations)

    # Position an ant in an environment
    def join(self, environment):
        self.environment = environment
