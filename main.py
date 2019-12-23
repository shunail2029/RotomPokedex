from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    FollowEvent, MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, CarouselColumn, CarouselTemplate
)
import os

import mydb

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

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    name_list = text.split('\n')
    columns = []
    head = ''
    is_first = True
    for name in name_list:
        name = name.strip()
        if not is_first:
            head += 'と'
        head += name
        results = mydb.get_pokemon(name)
        if len(results) == 0:
            columns.append(CarouselColumn(title=name), text='このなまえのポケモンは見つからなかったロ...')
        for result in results:
            columns.append(CarouselColumn(title=result[0], text=result[1]))

    head += 'の検索結果はこちらロト！'
    line_bot_api.reply_message(event.reply_token, [TextSendMessage(text=head), TemplateSendMessage(alt_text='Carousel template', template=CarouselTemplate(columns=columns))])

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
