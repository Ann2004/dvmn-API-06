# Automated posting of comics in Telegram

Get [xkcd](https://xkcd.com/) comics and automate your Telegram posting if you don't have time to run a channel yourself.


## Installation

Create a `.env` file in the project directory and add your Telegram bot token and chat id:
```
TG_TOKEN=your_tg_access_token
TG_CHAT_ID=your_chat_id
```

- Create your Telegram bot using [BotFather](https://telegram.me/BotFather) and get the bot's API token.
- The chat_id of a channel is a link to it, for example: @dvmn_flood. You also need to make the bot a channel admin.

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```


## Example usage

### Automated posting of a random [xkcd](https://xkcd.com/) comic to Telegram channel once in several hours:
Publication frequency - number of delay hours can be changed. Run the script from the command line, providing the number of hours as an argument.
```
python post_photos_to_tg.py -H <number_of_hours>
```
- If no argument is specified, by default photos will be posted one every 4 hours.


## Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
