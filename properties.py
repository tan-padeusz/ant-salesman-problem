from os import path


class Keys:
    __COLONY_SIZE_KEY = "COLONY_SIZE"
    __DATA_FILE_DELIMITER_KEY = "DATA_FILE_DELIMITER"
    __DATA_FILE_PATH_KEY = "DATA_FILE_PATH"
    __ITERATION_NUMBER_KEY = "ITERATION_NUMBER"
    __PHEROMONES_DEPOSIT_AMOUNT_KEY = "PHEROMONES_DEPOSIT_AMOUNT"
    __PHEROMONES_EVAPORATION_COEFFICIENT_KEY = "PHEROMONES_EVAPORATION_COEFFICIENT"
    __PHEROMONES_INITIAL_AMOUNT_KEY = "PHEROMONES_INITIAL_AMOUNT"

    __all_keys = [
        __COLONY_SIZE_KEY,
        __DATA_FILE_DELIMITER_KEY,
        __DATA_FILE_PATH_KEY,
        __ITERATION_NUMBER_KEY,
        __PHEROMONES_DEPOSIT_AMOUNT_KEY,
        __PHEROMONES_EVAPORATION_COEFFICIENT_KEY,
        __PHEROMONES_INITIAL_AMOUNT_KEY
    ]

    @staticmethod
    def get_data_file_path_key() -> str:
        return Keys.__DATA_FILE_PATH_KEY

    @staticmethod
    def get_data_file_delimiter_key() -> str:
        return Keys.__DATA_FILE_DELIMITER_KEY

    @staticmethod
    def get_pheromones_initial_amount_key() -> str:
        return Keys.__PHEROMONES_INITIAL_AMOUNT_KEY

    @staticmethod
    def get_iteration_number_key() -> str:
        return Keys.__ITERATION_NUMBER_KEY

    @staticmethod
    def get_colony_size_key() -> str:
        return Keys.__COLONY_SIZE_KEY

    @staticmethod
    def get_pheromones_deposit_amount_key() -> str:
        return Keys.__PHEROMONES_DEPOSIT_AMOUNT_KEY

    @staticmethod
    def get_pheromones_evaporation_coefficient_key() -> str:
        return Keys.__PHEROMONES_EVAPORATION_COEFFICIENT_KEY

    @staticmethod
    def get_all_keys() -> list[str]:
        return Keys.__all_keys


class Properties:
    class Error(Exception):
        def __init__(self, message: str):
            self.__message = message

        def get_message(self):
            return self.__message

    def __init__(self, file_path: str):
        super().__init__()
        properties = {}
        self.__error = ""
        try:
            Properties.__validate_file_path(file_path)
            file_content = Properties.__load_file_content(file_path)
            properties = Properties.__load_properties_from_file_content(file_content)
            Validator.validate_properties(properties)
        except Properties.Error as error:
            base_error = "Error while loading properties file!\n"
            self.__error = base_error + error.get_message()
        except Validator.Error as error:
            base_error = "Error while loading properties file!\n"
            self.__error = base_error + error.get_message()
        finally:
            self.__properties = properties

    def has_error(self) -> bool:
        return self.__error != ""

    def get_error(self) -> str:
        return self.__error

    @staticmethod
    def __validate_file_path(file_path: str):
        if file_path is None or file_path == "":
            raise Properties.Error("File path is empty!")
        if not path.isfile(file_path):
            italic_file_path = "\x1B[3m" + file_path + "\x1B[0m"
            raise Properties.Error("File " + italic_file_path + " does not exist!")
        if not file_path.endswith(".properties"):
            italic_extension = "\x1B[3m.properties\x1B[0m"
            raise Properties.Error("File is not " + italic_extension + " file!")

    @staticmethod
    def __load_file_content(file_path: str) -> list[str]:
        file = open(file_path)
        lines = []
        for line in file:
            lines.append(line.strip())
        file.close()
        return lines

    @staticmethod
    def __load_properties_from_file_content(file_content: list[str]) -> dict[str, str]:
        properties = {}
        for index in range(len(file_content)):
            line = file_content[index]
            split_line = line.split("=")
            if len(split_line) != 2:
                raise Properties.Error("Invalid values at row " + str(index + 1) + "! Expected KEY=VALUE format!")
            properties[split_line[0].strip()] = split_line[1].strip()
        return properties

    def get_str_property(self, key: str) -> str:
        return self.__properties[key]

    def get_int_property(self, key: str) -> int:
        return int(self.__properties[key])

    def get_float_property(self, key: str) -> float:
        return float(self.__properties[key])


class Validator:
    class Error(Exception):
        def __init__(self, message):
            self.__message = message

        def get_message(self):
            return self.__message

    @staticmethod
    def validate_properties(properties: dict[str, str]):
        Validator.__validate_properties_existence(properties)
        Validator.__validate_properties_values(properties)

    @staticmethod
    def __is_str_none_or_empty(value: str) -> bool:
        return value is None or value == ""

    @staticmethod
    def __validate_properties_existence(properties: dict[str, str]):
        for key in Keys.get_all_keys():
            if key not in properties:
                raise Validator.Error(f"{key} key not found in properties file!")
            if Validator.__is_str_none_or_empty(properties[key]):
                raise Validator.Error(f"Value for {key} key is empty!")

    @staticmethod
    def __validate_properties_values(properties: dict[str, str]):
        Validator.__validate_colony_size_value(properties)
        Validator.__validate_data_file_delimiter_value(properties)
        Validator.__validate_data_file_path_value(properties)
        Validator.__validate_iteration_number_value(properties)
        Validator.__validate_pheromones_deposit_amount_value(properties)
        Validator.__validate_pheromones_evaporation_coefficient_value(properties)
        Validator.__validate_pheromones_initial_amount_value(properties)

    @staticmethod
    def __validate_colony_size_value(properties: dict[str, str]):
        value = properties[Keys.get_colony_size_key()]
        try:
            value = int(value)
            if value < 1:
                raise Validator.Error("Value of colony size must be greater than 0!")
        except ValueError:
            raise Validator.Error("Value of colony size is not an integer!")

    @staticmethod
    def __validate_data_file_delimiter_value(properties: dict[str, str]):
        value = properties[Keys.get_data_file_delimiter_key()]
        if len(value) != 1:
            raise Validator.Error("Value of data file delimiter should be single character!")

    @staticmethod
    def __validate_data_file_path_value(properties: dict[str, str]):
        value = properties[Keys.get_data_file_path_key()]
        if not value.endswith(".csv"):
            raise Validator.Error("Data file should be .csv file!")

    @staticmethod
    def __validate_iteration_number_value(properties: dict[str, str]):
        value = properties[Keys.get_iteration_number_key()]
        try:
            value = int(value)
            if value < 1:
                raise Validator.Error("Value of iteration number must be greater than 0!")
        except ValueError:
            raise Validator.Error("Value of iteration number is not an integer!")

    @staticmethod
    def __validate_pheromones_deposit_amount_value(properties: dict[str, str]):
        value = properties[Keys.get_pheromones_deposit_amount_key()]
        try:
            value = float(value)
            if value <= 0:
                raise Validator.Error("Value of pheromones deposit amount must be greater than 0!")
        except ValueError:
            raise Validator.Error("Value of pheromones deposit amount is not a number!")

    @staticmethod
    def __validate_pheromones_evaporation_coefficient_value(properties: dict[str, str]):
        value = properties[Keys.get_pheromones_evaporation_coefficient_key()]
        try:
            value = float(value)
            if value <= 0 or value >= 1:
                raise Validator.Error("Value of pheromones evaporation coefficient must be between 0 and 1!")
        except ValueError:
            raise Validator.Error("Value of pheromones evaporation coefficient is not a number!")

    @staticmethod
    def __validate_pheromones_initial_amount_value(properties: dict[str, str]):
        value = properties[Keys.get_pheromones_initial_amount_key()]
        try:
            value = float(value)
            if value <= 0:
                raise Validator.Error("Value of initial pheromones amount must be greater than 0!")
        except ValueError:
            raise Validator.Error("Value of initial pheromones is not a number!")
