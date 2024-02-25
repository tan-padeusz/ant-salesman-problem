from grid import DistanceGrid, PheromoneGrid
from random import randrange, random


class Ant:
    def __init__(self, distance_grid: DistanceGrid, pheromone_grid: PheromoneGrid):
        route = []
        travelled_distance = 0.0
        possible_destinations = list(range(distance_grid.get_size()))
        starting_point = randrange(len(possible_destinations))
        route.append(starting_point)
        del possible_destinations[starting_point]
        while len(possible_destinations) > 0:
            pheromone_sum = Ant.__sum_possible_routes_pheromones(pheromone_grid, route[-1], possible_destinations)
            for index in range(len(possible_destinations)):
                possible_destination = possible_destinations[index]
                destination_pheromone = pheromone_grid.pheromones_between(route[-1], possible_destination)
                random_float = random()
                if random_float < (destination_pheromone / pheromone_sum):
                    route.append(possible_destination)
                    travelled_distance += distance_grid.distance_between(route[-2], route[-1])
                    del possible_destinations[index]
                    break
                else:
                    pheromone_sum -= destination_pheromone

        travelled_distance += distance_grid.distance_between(route[-1], route[0])
        self.__route = route
        self.__travelled_distance = travelled_distance

    def get_route(self) -> list[int]:
        return self.__route

    def get_natural_route(self) -> list[int]:
        route_copy = self.__route.copy()
        for index in range(len(route_copy)):
            route_copy[index] += 1
        return route_copy

    def get_travelled_distance(self) -> float:
        return self.__travelled_distance

    @staticmethod
    def __sum_possible_routes_pheromones(pheromone_grid: PheromoneGrid, start: int, possible_destinations: list[int]) -> float:
        pheromone_sum = 0.0
        for possible_destination in possible_destinations:
            pheromone_sum += pheromone_grid.pheromones_between(start, possible_destination)
        return pheromone_sum


class Colony:
    def __init__(self, size: int, distance_grid: DistanceGrid, pheromone_grid: PheromoneGrid):
        ants = []
        best_ant = None
        for index in range(size):
            ant = Ant(distance_grid, pheromone_grid)
            if best_ant is None or ant.get_travelled_distance() < best_ant.get_travelled_distance():
                best_ant = ant
            ants.append(ant)
        self.__ants = ants
        self.__best_ant = best_ant

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self) -> Ant:
        colony_size = len(self.__ants)
        if self.__index < colony_size:
            ant = self.__ants[self.__index]
            self.__index += 1
            return ant
        else:
            raise StopIteration

    def get_best_ant(self) -> Ant:
        return self.__best_ant

