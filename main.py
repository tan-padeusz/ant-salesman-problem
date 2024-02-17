from FileHandler import FileHandler


if __name__ == "__main__":
    file_path = "test_file.txt"
    delimiter = ";"
    matrix, error = FileHandler.load_file(file_path, delimiter)
    if error:
        print(error)
    else:
        print("Loading was successful!")
