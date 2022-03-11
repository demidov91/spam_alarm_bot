import sys

from telegram import Bot

from spam_bot.defines import TOKEN, SECURE_URL


bot = Bot(TOKEN)


def run(host):
    with open('YOURPUBLIC.pem', 'rb') as f:
        cert = f.read()

    print(
        bot.set_webhook(
            f'https://{host}/spam_bot/{SECURE_URL}/',
            certificate=cert,
        ),
    )
    print(bot.get_webhook_info())


def remove_webhook():
    print(bot.set_webhook(''))
    print(bot.get_webhook_info())


def get_webhook():
    print(bot.get_webhook_info())


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] != '?':
            run(sys.argv[1])

        else:
            get_webhook()

    else:
        remove_webhook()

