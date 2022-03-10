from flask import Flask, request

from spam_bot.controller import detector
from spam_bot.defines import SECURE_URL

app = Flask(__name__)


@app.route(f'/spam_bot/{SECURE_URL}/', methods=['POST'])
def handler():
    return detector(request.get_json())


if __name__ == '__main__':
    app.run()
