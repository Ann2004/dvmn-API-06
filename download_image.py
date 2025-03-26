import requests
import get_file_name
from pathlib import Path


def download_image(image_url, payload=None):
    image_response = requests.get(image_url, params=payload)
    image_response.raise_for_status()
        
    file_name = get_file_name.get_file_name(image_url)
    
    Path("files").mkdir(parents=True, exist_ok=True) 
    with open(f'files/{file_name}', 'wb') as file:
        file.write(image_response.content)