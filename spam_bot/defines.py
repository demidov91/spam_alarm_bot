import os

BAD_STRINGS = [
    'парни',
    'парня',
    'парне',
    'всу',
    'зсу',
    'хлопц',
    'мужчин',
    'чоловік',
]

TOKEN = os.environ['TOKEN']
SECURE_URL = os.environ['SECURE_URL']


CHAT_TO_CHANNEL = {
    'hrushiv_help': '@spam_alarm_hrushiv',
    'krakivets_help': '@spam_alarm_krakivets',
    'rawa_ruska_help': '@spam_alarm_rawa_ruska',
    'ustyluh_help': '@spam_alarm_ustyluh',
    'shehyni_help': '@shehyni_alarm_bot',
    'yagodyn_help': '@spam_alarm_ustyluh',
    'uhryniv_help': '@spam_alarm_ustyluh',
    'smolnica_help': '@spam_alarm_ustyluh',
}
