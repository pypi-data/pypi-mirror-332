from pathlib import Path


def get_original_file_path(files):
    return Path(next(iter(files.values()))['meta']['path_original'])
