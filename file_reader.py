def read_file_as_str(path: str) -> str:
    return open(path, 'r').read()

def read_file_as_list_str(path: str) -> list[str]:
    with open(path, 'r') as file:
        return [line.strip() for line in file]
    
def read_file_as_int(path: str) -> list[int]:
    with open(path, 'r') as file:
        return [int(line.strip()) for line in file]