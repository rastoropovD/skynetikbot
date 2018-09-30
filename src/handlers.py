

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello! Let\'s talk about smth')


def textMessage(bot, update):
    print(update)
    response = 'Got Your message: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)