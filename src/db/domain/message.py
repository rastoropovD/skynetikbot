from mongoengine import connect, DynamicDocument, LongField, StringField
from src.db.config import MONGODB_CONFIG
connect(MONGODB_CONFIG['dbname'])


class Message(DynamicDocument):
    meta: {
        'collection': 'message'
    }
    requestChatId: LongField()
    requestFirstName: StringField()
    requestLastName: StringField()
    requestText: StringField()
    requestDate: LongField()
    responseChatId: LongField()
    responseText: StringField()
    responseDate: LongField()
