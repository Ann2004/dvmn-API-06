import telegram


def send_photo_to_chat(tg_token, chat_id, file_path, caption):
    bot = telegram.Bot(token=tg_token)
    
    with open(file_path, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file, caption=caption)