import argparse
from pathlib import Path
from telegram_bot.tg_bot import send_photo_to_chat
import os
import time
from dotenv import load_dotenv
from fetch_xkcd_comic import fetch_random_xkcd_comic
from delete_files_from_directory import delete_files_from_directory


def main():
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    
    parser = argparse.ArgumentParser(description='Post photos to Telegram')
    parser.add_argument('-H', '--hours', help='publication frequency - number delay hours', type=int, default=4)
    args = parser.parse_args()
    
    Path("files").mkdir(parents=True, exist_ok=True) 
    directory = Path('files')
    while True:
        try:
            comic_info = fetch_random_xkcd_comic()
            
            comic_caption = comic_info['alt']
            
            file_paths = [os.path.join(directory, filename) for filename in os.listdir(directory)]
            file_path = file_paths[0]
            
            send_photo_to_chat(tg_token, chat_id, file_path, comic_caption)
        finally:
            delete_files_from_directory(directory)
        
        time.sleep(args.hours * 3600)

if __name__ == '__main__':
    main()