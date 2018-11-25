# -*- coding:utf-8 -*-

import os
from bottle import route, run


@route('/', method="POST")
def hello():
    return '{"version":"1.0","response":{"outputSpeech":{"type":"SpeechList","values":[{"type":"PlainText","lang":"ja","value":"こんにちは テストスキルです"}]},"card":{},"directives":[],"shouldEndSession":true}}'


run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))