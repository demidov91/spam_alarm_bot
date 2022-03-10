import logging

from flask import Flask, request

from spam_bot.controller import detector
from spam_bot.defines import SECURE_URL

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route(f'/spam_bot/{SECURE_URL}/', methods=['POST'])
def handler():
    try:
        return detector(request.get_json())
    except:
        logger.exception('Unexpected exception.')
        return {}


if __name__ == '__main__':
    app.run()
