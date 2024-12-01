def read_file(path: str):
    with open(path, 'r') as file:
        return [line.strip() for line in file]
    
def read_file_as_int(path: str):
    with open(path, 'r') as file:
        return [int(line.strip()) for line in file]