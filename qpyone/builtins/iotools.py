from typing import Any


__all__ = ["copy_files", "read_as_str", "read_as_list", "write", "write_lines"]


def copy_files(file_path):
    with open(file_path) as f:
        result = f.readlines()
    new_result = []
    for item in result:
        if len(item) > 1:
            new_result.append(item)
    return new_result


def read_as_str(file_path: str, **kwargs) -> str:
    with open(file_path) as f:
        return "\n".join(f.readlines())


def read_as_list(file_path: str, **kwargs) -> list[str]:
    with open(file_path) as f:
        return f.readlines()


def write(content: str, file_path: str, **kwargs):
    with open(file_path, "w") as f:
        return f.write(content)


def write_lines(content: list[Any], file_path: str, **kwargs):
    with open(file_path, "w") as f:
        return f.writelines(content)
