import sys

from telegram import Bot

from spam_bot.defines import TOKEN, SECURE_URL


def run(host):
    print(Bot(TOKEN).set_webhook(f'https://{host}/spam_bot/{SECURE_URL}/'))


if __name__ == '__main__':
    run(sys.argv[1])
