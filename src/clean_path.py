import os

def clean_path(path: str) -> str:
    """ clean_path takes path and remove duplicated slash and dots from it

    Args:
        path (str): path to be cleaned

    Returns:
        str: new path with dots and duplicated slashes removed
    """
    path = os.path.abspath(path).replace('./', '/')
    slash = False
    new_path = ""
    for letter in path:
        if letter != "/":
            new_path += letter
            slash = False
        elif letter == "/" and slash:
            continue
        elif letter == "/" and not slash:
            new_path += "/"
            slash = True
    new_path = new_path.rstrip('/')
    return (new_path)