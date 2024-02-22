from telegram import Bot
from settings import TOKEN

def start(chat_id,name):
    bot=Bot(TOKEN)
    bot.sendMessage(chat_id=chat_id,text=f"Assalomu aleykum {name}!\nLazy Academy ga xush kelibsiz!")