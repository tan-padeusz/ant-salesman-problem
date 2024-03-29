from os import path


class DistanceGrid:
    class Error(Exception):
        def __init__(self, message: str = ""):
            self.__message = message

        def get_message(self) -> str:
            return self.__message

    def __init__(self, file_path: str, delimiter: str):
        super().__init__()
        italic_file_path = "\x1B[3m" + file_path + "\x1B[0m"
        base_error = "Error while loading data file " + italic_file_path + "!\n"
        grid = []
        self.__error = ""
        try:
            grid = DistanceGrid.__load_file_content_into_grid(file_path, delimiter)
            grid = DistanceGrid.__validate_grid_shape(grid)
            grid = DistanceGrid.__str_grid_to_float_grid(grid)
            grid = DistanceGrid.__set_zeroes_at_diagonal(grid)
        except DistanceGrid.Error as error:
            grid = []
            self.__error = base_error + error.get_message()
        finally:
            self.__confirm_success()
            self.__grid = grid
            self.__size = len(grid)

    def __confirm_success(self):
        if self.__error != "":
            print(self.__error)
            exit()

    def get_size(self) -> int:
        return self.__size

    def distance_between(self, start: int, stop: int) -> float:
        return self.__grid[start][stop]

    @staticmethod
    def __load_file_content_into_grid(file_path: str, delimiter: str) -> list[list[str]]:
        if not path.isfile(file_path):
            raise DistanceGrid.Error("File does not exist!")
        file = open(file_path)
        str_matrix = []
        for line in file:
            str_matrix.append(line.strip().split(delimiter))
        file.close()
        return str_matrix

    @staticmethod
    def __validate_grid_shape(str_grid: list[list[str]]) -> list[list[str]]:
        grid_size = len(str_grid)
        if not grid_size:
            raise DistanceGrid.Error("File is empty!")
        for index in range(grid_size):
            if len(str_grid[index]) != grid_size:
                raise DistanceGrid.Error("Invalid line length at line " + str(index + 1) + "!")
        return str_grid

    @staticmethod
    def __str_grid_to_float_grid(str_grid: list[list[str]]) -> list[list[float]]:
        float_grid = []
        for row_index in range(len(str_grid)):
            str_row = str_grid[row_index]
            float_row = []
            for column_index in range(len(str_row)):
                str_value = str_grid[row_index][column_index]
                float_value = DistanceGrid.__str_value_to_float_value(str_value)
                if float_value is None:
                    raise DistanceGrid.Error("Value at row " + str(row_index + 1) + ", column " + str(column_index + 1) + " is not a number!")
                float_row.append(float_value)
            float_grid.append(float_row)
        return float_grid

    @staticmethod
    def __str_value_to_float_value(str_value: str) -> float | None:
        try:
            return float(str_value)
        except ValueError:
            return None

    @staticmethod
    def __set_zeroes_at_diagonal(float_grid: list[list[float]]) -> list[list[float]]:
        size = len(float_grid)
        for index in range(size):
            float_grid[index][index] = 0
        return float_grid


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
