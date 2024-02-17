from DistanceGrid import DistanceGrid
from PheromoneGrid import PheromoneGrid
from Ant import Ant
from Colony import Colony

if __name__ == "__main__":
    file_path = "test_file.txt"
    delimiter = ";"
    initial_pheromones = 1.0
    iteration_number = 10000
    colony_size = 100
    delta_pheromone = 1.0
    rho = 0.6
    distance_grid = DistanceGrid(file_path, delimiter)
    pheromone_grid = PheromoneGrid(distance_grid.get_size(), initial_pheromones)
    best_ant = None
    for iteration in range(iteration_number):
        colony = Colony(colony_size, distance_grid, pheromone_grid)
        best_ant = colony.get_best_ant()
        for ant in colony:
            route = ant.get_route()
            for index in range(-1, len(route) - 1):
                distance = distance_grid.distance_between(route[index], route[index + 1])
                pheromone_grid.deposit_pheromones_between(route[index], route[index + 1], delta_pheromone / distance)
        pheromone_grid.evaporate_pheromones(rho)

    print("Route:", best_ant.get_route())
    print("Distance:", best_ant.get_distance())
