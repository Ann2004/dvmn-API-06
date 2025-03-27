import requests
import get_file_name
from pathlib import Path
import os


def download_image(image_url, payload=None):
    image_response = requests.get(image_url, params=payload)
    image_response.raise_for_status()
        
    file_name = get_file_name.get_file_name(image_url)
    
    path = Path('files') / file_name
    with open(path, 'wb') as file:
        file.write(image_response.content) 