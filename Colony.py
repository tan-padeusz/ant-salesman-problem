from Ant import Ant
from DistanceGrid import DistanceGrid
from PheromoneGrid import PheromoneGrid


class Colony:
    def __init__(self, size: int, distance_grid: DistanceGrid, pheromone_grid: PheromoneGrid):
        ants = []
        best_ant = None
        for index in range(size):
            ant = Ant(distance_grid, pheromone_grid)
            if best_ant is None or ant.get_distance() < best_ant.get_distance():
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

