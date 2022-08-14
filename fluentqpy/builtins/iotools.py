def read_as_str(file_path: str, **kwargs) -> str:
    with open(file_path, 'r') as f:
        return "\n".join(f.readlines())
