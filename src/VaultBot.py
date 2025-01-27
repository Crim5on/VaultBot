#!../venv/bin/python3.12

##
# file: VaultBot.py
#
# date: 2025-01-27
# author: Sandro Schnetzer
# contact: https://www.linkedin.com/in/sandroschnetzer/
# libraries: https://python-telegram-bot.org/
#
#
# Simple Telegram bot to enhance our flatshare's group chat.
# Bot listens to certain keywords and replies with the according answer
# specified in a json-dict.  
#
##


import logging, json

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters



# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)



def load_json(file: str) -> dict:
    with open(file) as filestream:
        json_dict = json.load(filestream)
        return json_dict

def read_token(file: str) -> str:
    with open(file) as tokenfile: 
        token = tokenfile.read()
        return token




def extract_words(sentence: str) -> list:
    words = sentence.split()
    return words

def clean_word(word: str) -> str:
    clean_word = ''.join(filter(str.isalnum, word))       # remove non-alphanumeric chars
    clean_word = clean_word.lower()
    return clean_word

def get_answer_from_keyword(dictionary: dict, sentence: str) -> str:
    words = extract_words(sentence)
    for word in words:  # TODO: check words in sentence from the back.
        answer = dictionary.get(clean_word(word), None)
        if answer is not None:
            return answer
    return None



# command handler
async def dict_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    answer = get_answer_from_keyword(dictionary, update.message.text)
    if answer is not None:
        await update.message.reply_text(answer)






def main() -> None:
    config = load_json("./config.json")
    token = read_token(config["tokenfile"])
    global dictionary
    dictionary = load_json(config["dictionary"])    #TODO: pass through

    application = Application.builder().token(token).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, dict_reply))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
