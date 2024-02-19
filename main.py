from Properties import properties
from DistanceGrid import DistanceGrid
from PheromoneGrid import PheromoneGrid
from Colony import Colony

if __name__ == "__main__":
    distance_grid = DistanceGrid(properties["DATA_FILE_PATH"], properties["DATA_FILE_DELIMITER"])
    pheromone_grid = PheromoneGrid(distance_grid.get_size(), properties["INITIAL_PHEROMONES"])
    best_ant = None
    for iteration in range(properties["ITERATION_NUMBER"]):
        colony = Colony(properties["COLONY_SIZE"], distance_grid, pheromone_grid)
        best_ant = colony.get_best_ant()
        for ant in colony:
            route = ant.get_route()
            for index in range(-1, len(route) - 1):
                distance = distance_grid.distance_between(route[index], route[index + 1])
                pheromones_delta = properties["PHEROMONES_DELTA"]
                pheromone_grid.deposit_pheromones_between(route[index], route[index + 1], pheromones_delta / distance)
        pheromone_grid.evaporate_pheromones(properties["PHEROMONES_EVAPORATION_RATE"])

    print("Route:", best_ant.get_natural_route())
    print("Distance:", best_ant.get_travelled_distance())
