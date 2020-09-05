from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    FlexSendMessage)
import os

from mypackage import mydb, myline

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
    notfound = ''
    cnt_bubble = 0
    for name in name_list:
        if not name:
            continue
        print('start to search ' + name)
        if head:
            head += 'と'
        head += name
        if cnt_bubble <= 10:
            result = mydb.get_pokemon(name)
            for res in result:
                if not res['success']:
                    if notfound:
                        notfound += 'と'
                    notfound += res['name']
                else:
                    results.append(res)
                    cnt_bubble += 1

    head += 'の検索結果はこちらロト！'
    if cnt_bubble == 0:
        print('no pokemon were found')
        line_bot_api.reply_message(
            event.reply_token, messages=[
                TextSendMessage(
                    text=head), TextSendMessage(
                    text=notfound + 'はみつからなかったロト...')])
    else:
        content = myline.get_flex_json(results)
        flexmessage = FlexSendMessage(alt_text='Good luck', contents=content)
        print('flexmessage > ')
        print(flexmessage)
        messages = [TextSendMessage(text=head), flexmessage]
        if notfound:
            messages.append(TextSendMessage(text=notfound + 'はみつからなかったロト...'))
        if cnt_bubble > 10:
            messages.append(TextSendMessage(text='検索結果が多すぎてぜんぶは表示できなかったロト...'))
        line_bot_api.reply_message(event.reply_token, messages=messages)


if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
