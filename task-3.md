# Task 3


## 1
The parameters $a$ and $b$ play an important role in determining the performance of the ant colony optimization algorithm. $a$ controls the relative importance of the pheromone trail compared to the heuristic information, while $b$ controls the relative importance of the distance between cities compared to the pheromone trail. In general, smaller values of $a$ lead to a stronger focus on heuristic information, while larger values of $b$ lead to a stronger focus on the pheromone trail. In my implementation, I found that $a$ = 1 seems to be ideal and values between 2 and 5 are good fit for $b$.


## 2
The evaporation rate $p$ also plays an important role in the performance of the ant colony optimization. It determines how fast the pheromone trail evaporates, which affects the balance between exploitation and exploration in the search process. Higher values of $p$ lead to faster evaporation and more focus on exploration, while lower values of $p$ lead to slower evaporation and more focus on exploitation. In my implementation, I found that the recommended value of $p$=0.5 gave good results in terms of finding near-optimal solutions for the TSP instances I tested. Decreasing $p$ below 0.5 resulted in a higher probability of ants getting stuck in local optima, while increasing $p$ above 0.5 did not result in significant improvements in the quality of solutions.


## 3
To apply the ant colony optimization algorithm to a dynamic traveling salesman problem (DTSP) where cities can be added or removed at runtime, the implementation would need to be modified to account for the changing problem instance. One possible approach is to periodically re-evaluate the pheromone trace values based on the current cities, using the existing pheromone values as a starting point. Another approach is to use a reactive update strategy, in which pheromone values are updated only when a city is added to or removed from the problem instance. This would involve re-evaluating the heuristic information and pheromone values for the edges associated with the added or removed city and updating the pheromone path accordingly.