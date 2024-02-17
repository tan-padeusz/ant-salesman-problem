class PheromoneGrid:
    def __init__(self, size: int, initial_pheromones: float):
        grid = []
        for row in range(size):
            row = []
            for column in range(size):
                if column == row:
                    row.append(0.0)
                else:
                    row.append(initial_pheromones)
            grid.append(row)
        self.__size = size
        self.__grid = grid

    def get_size(self) -> int:
        return self.__size

    def pheromones_between(self, start: int, stop: int) -> float:
        return self.__grid[start][stop]

    def deposit_pheromones_between(self, start: int, stop: int, value: float):
        self.__grid[start][stop] += value

    def evaporate_pheromones(self, rho: float):
        for row in range(self.__size):
            for column in range(self.__size):
                self.__grid[row][column] *= rho

