import logging

from telegram import Update, Bot

from spam_bot.defines import BAD_STRINGS, TOKEN, CHAT_TO_CHANNEL
from spam_bot.utils import contains_card_number


logger = logging.getLogger(__name__)


def detector(data: dict):
    update = Update.de_json(data, None)

    if not update.effective_user:
        return {}

    chat_id = update.effective_chat.id
    message = update.message

    if not message:
        return {}

    if _detect_message(message):
        recipient = CHAT_TO_CHANNEL.get(message.chat.username) or CHAT_TO_CHANNEL['krakivets_help']

        bot = Bot(TOKEN)
        if message.chat.username:
            logger.info(
                bot.send_message(
                    chat_id=recipient,
                    text=f'https://t.me/{message.chat.username}/{message.message_id}/',
                )
            )

        else:
            logger.info('No chat username.')

        logger.info(bot.forward_message(
            chat_id=recipient,
            from_chat_id=chat_id,
            message_id=message.message_id,
        ))

        return {}

    return {}


def _detect_message(message):
    if message.photo or message.video:
        return True

    if message.text:
        lower_text = message.text.lower()
        return any(x in lower_text for x in BAD_STRINGS) or contains_card_number(lower_text)
