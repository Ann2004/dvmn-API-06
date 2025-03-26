from urllib.parse import urlsplit, unquote
from os.path import split


def get_file_name(url):
    decoded_url = unquote(url)
    image_path = urlsplit(decoded_url).path
    file_name = split(image_path)[1]
    return file_name