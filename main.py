from DistanceGrid import DistanceGrid


if __name__ == "__main__":
    file_path = "test_file.txt"
    delimiter = ";"
    grid = DistanceGrid(file_path, delimiter)
    if grid.has_error():
        print(grid.get_error())
    else:
        print("Distance grid created successfully!")
