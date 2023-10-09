import gzip
import os.path
import requests
import shutil


def download_file(url: str) -> None:
    local_filename = url.split('/')[-1]  # e.g. "warc.paths.gz"
    local_file_dir = url.split('/')[-2]  # e.g. "CC-MAIN-2013-20"
    local_file_dir_path = f"../data/{local_file_dir}/"  # e.g. ./data/CC-MAIN-2013-20
    local_file_path = f"../data/{local_file_dir}/{local_filename}"  # e.g. ./data/CC-MAIN-2013-20/warc.paths.gz

    # Check if file already exists,
    # TODO: maybe also check for matching checksum
    if os.path.isfile(local_file_path):
        print("File already exists")
        return

    # create directory if it doesn't exist
    if not os.path.isdir(local_file_dir_path):
        print(f"Creating directory {local_file_dir_path}")
        os.mkdir(local_file_dir_path)

    # Download file. To not use too much memory using method from
    # https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
    print(f"Downloading File to {local_file_path}")
    with requests.get(url, stream=True) as r:
        with open(local_file_path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    print("Done.")

    return
