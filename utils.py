def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.rstrip("\r\n") for line in file]


