from typing import List, Any


def copy_files(file_path):
    with open(file_path, 'r') as f:
        result = f.readlines()
    new_result = []
    for item in result:
        if len(item) > 1:
            new_result.append(item)
    return new_result


def read_as_str(file_path: str, **kwargs) -> str:
    with open(file_path, 'r') as f:
        return "\n".join(f.readlines())


def read_as_list(file_path: str, **kwargs) -> List[str]:
    with open(file_path, 'r') as f:
        return f.readlines()


def write(content: str, file_path: str, **kwargs):
    with open(file_path, 'w') as f:
        return f.write(content)


def write_lines(content: List[Any], file_path: str, **kwargs):
    with open(file_path, 'w') as f:
        return f.writelines(content)
