from telegram import Update, Bot

from spam_bot.defines import BAD_STRINGS, CHAT_TO_SEND, TOKEN


def detector(data: dict):
    update = Update.de_json(data, None)

    if not update.effective_user:
        return {}

    chat_id = update.effective_chat.id
    message = update.message

    if not message:
        return {}

    if _detect_message(message):
        data = {
            'chat_id': CHAT_TO_SEND,
            'from_chat_id': chat_id,
            'message_id': message.message_id,
        }
        bot = Bot(TOKEN)
        if message.chat.username:
            print(
                bot.send_message(
                    chat_id=CHAT_TO_SEND,
                    text=f'https://t.me/{message.chat.username}/{message.message_id}/',
                )
            )

        else:
            print('No chat username.')

        print(bot.forward_message(**data))

        return {}

    return {}


def _detect_message(message):
    if message.photo or message.video:
        return True

    if message.text:
        lower_text = message.text.lower()
        return any(x in lower_text for x in BAD_STRINGS)


