from DistanceGrid import DistanceGrid
from PheromoneGrid import PheromoneGrid
from Ant import Ant

if __name__ == "__main__":
    file_path = "test_file.txt"
    delimiter = ";"
    initial_pheromones = 1.0
    iteration_number = 10000
    ant_number = 100
    delta_pheromone = 1.0
    rho = 0.6
    distance_grid = DistanceGrid(file_path, delimiter)
    pheromone_grid = PheromoneGrid(distance_grid.get_size(), initial_pheromones)
    ants = []
    best_ant = None
    for iteration in range(iteration_number):
        ants.clear()
        for ant_index in range(ant_number):
            ants.append(Ant(distance_grid, pheromone_grid))

        for ant in ants:
            if best_ant is None or ant.get_distance() < best_ant.get_distance():
                best_ant = ant
            route = ant.get_route()
            for index in range(-1, len(route) - 1):
                distance = distance_grid.get_distance(route[index], route[index + 1])
                pheromone_grid.deposit_pheromones_at(route[index], route[index + 1], delta_pheromone / distance)

        pheromone_grid.evaporate_pheromones(rho)

    print("Route:", best_ant.get_route())
    print("Distance:", best_ant.get_distance())

