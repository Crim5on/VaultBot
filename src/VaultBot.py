#!../venv/bin/python3.12

##
# file: VaultBot.py
#
# date: 2025-01-26
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


import logging

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters



# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)





def read_token(file: str) -> str:
    with open(file) as tokenfile: 
        token = tokenfile.read()
        return token

# Define a few command handlers. These usually take the two arguments update and context.


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text + " - VaultBot")


def main() -> None:
    # Read Bot Token from File:
    token = read_token("./vaultbot.token")

    # Start the bot.Create the Application and pass it your bot's token.
    application = Application.builder().token(token).build()

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
