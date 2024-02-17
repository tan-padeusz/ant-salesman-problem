from os import path


class FileHandler:
    @staticmethod
    def load_file(file_path: str, delimiter: str) -> (list[list[str]], str):
        italic_file_path = "\x1B[3m" + file_path + "\x1B[0m"
        base_error = "Error while loading file " + italic_file_path + "!\n"
        matrix, error = FileHandler.__load_file_content_as_matrix(file_path, delimiter)
        if error:
            return matrix, base_error + error
        matrix, error = FileHandler.__validate_matrix_shape(matrix)
        if error:
            return matrix, base_error + error
        matrix, error = FileHandler.__str_matrix_to_float_matrix(matrix)
        if error:
            return matrix, base_error + error
        return matrix, ""

    @staticmethod
    def __load_file_content_as_matrix(file_path: str, delimiter: str) -> (list[list[str]], str):
        if not path.isfile(file_path):
            return [], "File does not exist!"
        file = open(file_path)
        file_content = []
        for line in file:
            file_content.append(line.strip().split(delimiter))
        file.close()
        return file_content, ""

    @staticmethod
    def __validate_matrix_shape(str_matrix: list[list[str]]) -> (list[list[str]], str):
        file_length = len(str_matrix)
        if not file_length:
            return [], "File is empty!"
        for index in range(file_length):
            if len(str_matrix[index]) != file_length:
                return [], "Invalid line length at line " + str(index + 1) + "!"
        return str_matrix, ""

    @staticmethod
    def __str_matrix_to_float_matrix(file_content: list[list[str]]) -> (list[list[float]], str):
        matrix = []
        for line_index in range(len(file_content)):
            str_line = file_content[line_index]
            float_line = []
            for value_index in range(len(str_line)):
                float_value = FileHandler.__str_value_to_float_value(str_line[value_index])
                if not float_value:
                    return [], "Error at line " + str(line_index + 1) + ", column " + str(value_index + 1) + "! Value is not a number!"
                float_line.append(float_value)
            matrix.append(float_line)
        return matrix, ""

    @staticmethod
    def __str_value_to_float_value(str_value: str) -> float | None:
        try:
            return float(str_value)
        except ValueError:
            return None
