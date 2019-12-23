from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, FlexSendMessage
)
import os
import json

import mydb
import myline

app = Flask(__name__)

# 環境変数取得
CHANNEL_ACCESS_TOKEN = os.environ['CHANNEL_ACCESS_TOKEN']
CHANNEL_SECRET = os.environ['CHANNEL_SECRET']

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    print('callback\nbody: ' + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    name_list = text.split('\n')
    results = []
    head = ''
    is_first = True
    for name in name_list:
        name = name.strip()
        if not is_first:
            head += 'と'
        head += name
        result = mydb.get_pokemon(name)
        results.append(result)

    head += 'の検索結果はこちらロト！'
    content = json.loads((json.dumps(myline.get_flex_json(results))))
    flexmessage = FlexSendMessage(alt_text='hello', contents=content)
    print('flexmessage > ')
    print(flexmessage)
    line_bot_api.reply_message(event.reply_token, messages=[TextSendMessage(text=head), flexmessage])

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
