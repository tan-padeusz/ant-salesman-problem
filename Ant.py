from DistanceGrid import DistanceGrid
from PheromoneGrid import PheromoneGrid
from random import randrange, random


class Ant:
    def __init__(self, distance_grid: DistanceGrid, pheromone_grid: PheromoneGrid):
        route = []
        distance = 0.0
        possible_destinations = list(range(distance_grid.get_size()))
        starting_point = randrange(len(possible_destinations))
        route.append(starting_point)
        del possible_destinations[starting_point]
        while len(possible_destinations) > 0:
            pheromone_sum = Ant.__sum_possible_routes_pheromones(pheromone_grid, route[-1], possible_destinations)
            for index in range(len(possible_destinations)):
                possible_destination = possible_destinations[index]
                destination_pheromone = pheromone_grid.get_pheromones_at(route[-1], possible_destination)
                random_float = random()
                if random_float < (destination_pheromone / pheromone_sum):
                    route.append(possible_destination)
                    distance += distance_grid.get_distance(route[-2], route[-1])
                    del possible_destinations[index]
                    break
                else:
                    pheromone_sum -= destination_pheromone

        distance += distance_grid.get_distance(route[-1], route[0])
        self.__route = route
        self.__distance = distance

    def get_route(self) -> list[int]:
        return self.__route

    def get_distance(self) -> float:
        return self.__distance

    @staticmethod
    def __sum_possible_routes_pheromones(pheromone_grid: PheromoneGrid, start: int, possible_destinations: list[int]) -> float:
        pheromone_sum = 0.0
        for possible_destination in possible_destinations:
            pheromone_sum += pheromone_grid.get_pheromones_at(start, possible_destination)
        return pheromone_sum
