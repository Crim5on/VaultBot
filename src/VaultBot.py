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
# specified in a json dictionary.  
#
##


import logging, json, time
from typing import Optional

from telegram import ForceReply, Update, ChatMember, ChatMemberUpdated
from telegram.constants import ParseMode
from telegram.ext import Application, ContextTypes, MessageHandler, filters, ChatMemberHandler


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

def clean_word(word: str) -> str:
    clean_word = ''.join(filter(str.isalnum, word))       # remove non-alphanumeric chars
    clean_word = clean_word.lower()
    return clean_word

def get_answer_from_keyword(dictionary: dict, sentence: str) -> str:
    words = sentence.split()
    words = reversed(words)
    for word in words:
        answer = dictionary.get(clean_word(word), None)
        if answer is not None:
            return answer
    return None

def extract_status_change(chat_member_update: ChatMemberUpdated) -> Optional[tuple[bool, bool]]:
    status_change = chat_member_update.difference().get("status")
    old_is_member, new_is_member = chat_member_update.difference().get("is_member", (None, None))
    if status_change is None:
        return None
    old_status, new_status = status_change
    was_member = old_status in [ ChatMember.MEMBER, ChatMember.OWNER, ChatMember.ADMINISTRATOR, 
    ] or (old_status == ChatMember.RESTRICTED and old_is_member is True)
    is_member = new_status in [ ChatMember.MEMBER, ChatMember.OWNER, ChatMember.ADMINISTRATOR,
    ] or (new_status == ChatMember.RESTRICTED and new_is_member is True)
    return was_member, is_member




# command handler for dictionary
async def dict_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    answer = get_answer_from_keyword(dictionary, update.message.text)
    if answer is not None:
        time.sleep(1)   # makes it more human
        #await update.message.reply_text(answer)    # replies to message directly
    await context.bot.send_message(chat_id=update.message.chat_id, text=answer)


# command handler for greeting
async def greet_chat_members(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    result = extract_status_change(update.chat_member)
    if result is None:
        return
    was_member, is_member = result
    member_name = update.chat_member.new_chat_member.user.mention_html()
    if not was_member and is_member:
        await update.effective_chat.send_message(
            f"{member_name} is moving into the greatest Vault at COLIVE! Welcome :)", parse_mode=ParseMode.HTML,
        )
    elif was_member and not is_member:
        await update.effective_chat.send_message(
            f"{member_name} moved out of the greatest Vault at COLIVE :(", parse_mode=ParseMode.HTML,
        )




def main() -> None:
    config = load_json("./config.json")
    token = read_token(config["tokenfile"])
    global dictionary
    dictionary = load_json(config["dictionary"])    #TODO: pass through

    application = Application.builder().token(token).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, dict_reply))
    application.add_handler(ChatMemberHandler(greet_chat_members, ChatMemberHandler.CHAT_MEMBER))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

