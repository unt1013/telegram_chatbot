from flask import Flask, render_template, request
from decouple import config
import requests
import random

app = Flask(__name__)

token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
url = "https://api.telegram.org/bot"

@app.route('/send')
def send():
    text = request.args.get("text")
    requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')

@app.route('/write')
def write():
    return render_template('write.html')

@app.route(f'/{token}', methods=['POST'])
def telegram():
    text = request.get_json()['message']['text']
    chat_id = request.get_json()['message']['chat']['id']
    return_text = '알아듣게 하렴'
    if text == "안녕" :
        return_text = "안녕 못한데?"
    elif text == "주사위" :
        num = random.choice(range(1,100))
        return_text = num
    elif text == "코드" :
        return_text = "https://www.guitartricks.com/chords"
    requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={return_text}')
    
    return "ok", 200

if __name__ == ("__main__"):
    app.run(debug=True)