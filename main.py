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
    name_list = text.split()
    results = []
    head = ''
    is_first = True
    cnt_bubble = 0
    for name in name_list:
        if not name:
            continue
        print('start to search ' + name)
        if not is_first:
            head += 'と'
        head += name
        result = mydb.get_pokemon(name)
        results.append(result)
        is_first = False
        cnt_bubble += len(result)
        if cnt_bubble > 10:
            break

    if cnt_bubble == 0:
        print('no pokemon name received')
        line_bot_api.reply_message(event.reply_token, messages=[TextSendMessage(text='どのポケモンについて知りたいか教えてほしいロト！')])
    else:
        head += 'の検索結果はこちらロト！'
        content = myline.get_flex_json(results)
        flexmessage = FlexSendMessage(alt_text='hello', contents=content)
        print('flexmessage > ')
        print(flexmessage)
        if cnt_bubble <= 10:
            line_bot_api.reply_message(event.reply_token, messages=[TextSendMessage(text=head), flexmessage])
        else:
            line_bot_api.reply_message(event.reply_token, messages=[TextSendMessage(text=head), flexmessage, TextSendMessage(text='検索結果が多すぎてぜんぶは表示できなかったロト...')])

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
