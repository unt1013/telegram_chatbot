from decouple import config
import requests

token = config('TELEGRAM_BOT_TOKEN')
url = "https://api.telegram.org/bot"
ngrok_url = 'https://325f56f3.ngrok.io'

data =requests.get(f'{url}{token}/setwebhook?url={ngrok_url}/{token}')

print(data.text)