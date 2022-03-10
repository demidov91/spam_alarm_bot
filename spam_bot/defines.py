import os

BAD_STRINGS = [
    'парни',
    'парня',
    'парне',
    'всу',
    'зсу',
    'хлопц',
]

CHAT_TO_SEND = os.environ['CHAT_TO_SEND']
TOKEN = os.environ['TOKEN']
SECURE_URL = os.environ['SECURE_URL']