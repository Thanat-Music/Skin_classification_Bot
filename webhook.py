import json
from flask import Flask, request
from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError
from get_image import get_image
# from classifier import classifier

channel_acc_token ="RUYr3K+qxKWm10gaor6rR3kD74zofsWoNzQbhbooG6VA9wEeAzu0xSEszHCvsNf/o5qQsdfumK1svVVcFqPdpLbjFFOeIzA9xdPw2WO1BudbJQNQ8yHK1fFveDJDw9Q5eVkSZYpHAtXqhn/sMoHmtwdB04t89/1O/w1cDnyilFU="
line_bot_api = LineBotApi(channel_acc_token)


app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    response = request.get_json()
    if len(response['events'])>0:
        if response['events'][0]['message']['type']=="image":
            reply(response)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    
def reply(response):
    # text = response['events'][0]['message']['text']
    reply_token = response['events'][0]['replyToken']
    meassageID = response['events'][0]['message']['id']
    user_id = response['events'][0]['source']['userId']
    
    image = get_image(meassageID)
    # ans = model.classify(image)
    ans = "Normal"
    try:
        # send image message
        # line_bot_api.push_message(
        #     'USER_ID',
        #     ImageSendMessage(
        #         original_content_url='https://example.com/original.jpg',
        #         preview_image_url='https://example.com/preview.jpg'
        #     )
        # )
        if ans == "Normal":
            line_bot_api.reply_message(reply_token, TextSendMessage(text=f"จากรูปที่ส่งมา คุณผิวหนังของคุณปกติ"))
        elif ans == "Undefined":
            line_bot_api.reply_message(reply_token, TextSendMessage(text=f"จากรูปที่ส่งมา คาดว่าน่าจะเป็นโรคที่ผมไม่รู้จัก"))
        else: 
            line_bot_api.reply_message(reply_token, TextSendMessage(text=f"จากรูปที่ส่งมา คุณมีโอกาสเป็นโรค {str(ans)}"))
        line_bot_api.push_message(user_id, TextSendMessage(text='อย่างไรก็ตามนี่เป็นกระเมิณผลเบื้องต้นเท่านั้น คุณควรปรึกษาผู้เชี่ยวชาญอีกครั้งเพื่อความมั่นใจ'))

    except LineBotApiError as e:
        print(e)

if __name__ == '__main__':
    # model = classifier()
    app.run(host='0.0.0.0', port=5000)
