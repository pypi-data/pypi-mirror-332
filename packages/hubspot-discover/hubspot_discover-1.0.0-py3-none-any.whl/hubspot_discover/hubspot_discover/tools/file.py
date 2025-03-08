import os


def create_file(file_path: str, contents: list):
    """
    Creates an empty file, ensuring that the necessary directories exist.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        for content in contents:
            file.write(content)


def append_content(file_path, content):
    """
    Appends content to the file.
    """
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(content + "\n")


def append_generated_header(file_path):
    """
    Appends generated header to the file.
    """
    with open(file_path, "a", encoding="utf-8") as file:
        file.write("# GENERATED FILE DON'T UPDATE")
