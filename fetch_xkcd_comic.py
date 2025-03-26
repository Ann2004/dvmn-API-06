import requests
import download_image
import random


def get_comics_total():
    last_comic_url = 'https://xkcd.com/info.0.json'
    response = requests.get(last_comic_url)
    response.raise_for_status()
    comics_total = response.json()['num']
    return comics_total
        
        
def fetch_random_xkcd_comic():
    comics_total = get_comics_total()
    random_numer = random.randint(1, comics_total)
    
    response = requests.get(f'https://xkcd.com/{random_numer}/info.0.json')
    response.raise_for_status()
    comic_info = response.json()
    
    download_image.download_image(comic_info['img'])
    return comic_info