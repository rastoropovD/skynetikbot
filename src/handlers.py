from src.db.domain.message import Message
import apiai, json, os


def startCommand(bot, update):
    try:
        resp_msg = bot.send_message(chat_id=update.message.chat_id, text='Поговорим?')
        save_message(update.message, resp_msg)
    except Exception as e:
        print('startCommand error: ' + str(e))


def textMessage(bot, update):
    try:
        request = apiai.ApiAI(os.environ['API_AI_TOKEN']).text_request()
        request.lang = 'ru'
        request.session_id = update.message.chat_id
        request.query = update.message.text

        responseJson = json.loads(request.getresponse().read().decode('utf-8'))
        response = responseJson['result']['fulfillment']['speech']

        resp_msg = None
        if response:
            resp_msg = bot.send_message(chat_id=update.message.chat_id, text=response)
        else:
            resp_msg = bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')
        save_message(update.message, resp_msg)
    except Exception as e:
        print('textMessage Error: ' + str(e))


def save_message(message, resp_msg):
    print('New message [' + message.text + '] from ' + str(message.from_user.id))
    print('New response [' + resp_msg.text + '] from ' + str(resp_msg.from_user.id))
    Message(requestChatId=message.from_user.id,
            requestFirstName=message.from_user.first_name,
            requestLastName=message.from_user.last_name,
            reqtestText=message.text,
            requestDate=message.date,
            responseText=resp_msg.text,
            responseChatId=resp_msg.from_user.id,
            responseDate=resp_msg.date).save()
