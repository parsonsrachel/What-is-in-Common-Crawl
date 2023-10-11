import gzip
import os.path
import requests
import shutil


def download_file(url: str, decompress: bool = False) -> str:  # TODO: os.paht
    local_filename = url.split('/')[-1]  # e.g. "warc.paths.gz"
    local_file_dir = url.split('/')[-2]  # e.g. "CC-MAIN-2013-20"
    local_file_dir_path = f"../data/{local_file_dir}/"  # e.g. ./data/CC-MAIN-2013-20
    local_file_path = f"../data/{local_file_dir}/{local_filename}"  # e.g. ./data/CC-MAIN-2013-20/warc.paths.gz

    # Check if file already exists,
    # TODO: maybe also check for matching checksum
    if os.path.isfile(local_file_path):
        if decompress:
            return decompress_gz(local_file_path)
        return local_file_path

    # create directory if it doesn't exist
    if not os.path.isdir(local_file_dir_path):
        os.mkdir(local_file_dir_path)

    # Download file. To not use too much memory using method from
    # https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
    with requests.get(url, stream=True) as r:
        with open(local_file_path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    if decompress:
        return decompress_gz(local_file_path)

    return local_file_path


def decompress_gz(gz_path: str) -> os.path:  # TODO: os.pats
    """
    Decompresses .gz compressed file. As common crawl hosts only compressed files.
    Saves decompressed file in same path as compressed file.
    """
    decompressed_path = os.path.splitext(gz_path)[0]

    # Check if file already exists,
    # TODO: maybe also check for matching checksum
    if os.path.isfile(decompressed_path):
        return decompressed_path

    # unzip with gzip using
    # https://stackoverflow.com/questions/31028815/how-to-unzip-gz-file-using-python#44712152
    with gzip.open(gz_path, 'rb') as f_in:
        with open(decompressed_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    return decompressed_path
