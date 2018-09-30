from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from src.handlers import *
import os

updater = Updater(token=os.environ['API_TOKEN'])
dispatcher = updater.dispatcher

start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()
