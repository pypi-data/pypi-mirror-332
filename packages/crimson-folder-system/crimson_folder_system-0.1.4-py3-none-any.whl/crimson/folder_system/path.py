def get_sliced_path(path: str, i: int=0, j: int = None) -> str:
    split = path.split("/")
    
    if j is None:
        new_filename = "/".join(split[i:])
    else:
        new_filename = "/".join(split[i:j])
    
    return new_filename