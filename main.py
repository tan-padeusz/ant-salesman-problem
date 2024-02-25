from biology import Colony
from grid import DistanceGrid, PheromoneGrid
from properties import Keys, Properties

if __name__ == "__main__":
    properties = Properties("ant.properties")
    if properties.has_error():
        print(properties.get_error())
        exit()
    distance_grid = DistanceGrid(properties.get_str_property(Keys.get_data_file_path_key()), properties.get_str_property(Keys.get_data_file_delimiter_key()))
    if distance_grid.has_error():
        print(distance_grid.get_error())
        exit()
    pheromone_grid = PheromoneGrid(distance_grid.get_size(), properties.get_float_property(Keys.get_pheromones_initial_amount_key()))
    best_ant = None
    for iteration in range(properties.get_int_property(Keys.get_iteration_number_key())):
        colony = Colony(properties.get_int_property(Keys.get_colony_size_key()), distance_grid, pheromone_grid)
        best_ant = colony.get_best_ant()
        for ant in colony:
            route = ant.get_route()
            for index in range(-1, len(route) - 1):
                distance = distance_grid.distance_between(route[index], route[index + 1])
                pheromone_grid.deposit_pheromones_between(route[index], route[index + 1], properties.get_float_property(Keys.get_pheromones_deposit_amount_key()) / distance)
        pheromone_grid.evaporate_pheromones(properties.get_float_property(Keys.get_pheromones_evaporation_coefficient_key()))

    print("Route:", best_ant.get_natural_route())
    print("Distance:", best_ant.get_travelled_distance())
