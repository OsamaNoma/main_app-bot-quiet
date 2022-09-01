import binance.client
from binance.client import Client
import requests
import Telegram_bot as Tb


Pkey = 'Rwiro5P8sM3T1lFvq08276Edwo9viV8cbxIFqEq4mzzLPC25rVL67Vthj6UVBUNN'
Skey = 'Mq5UIuIZLxguP7BanbTp0dPdescemXnSjkWPzvlpNFcWRJMPzr4z78ECyzWLKtDQ'

client = Client(api_key=Pkey, api_secret=Skey) 

base_url = "https://api.binance.com"
endpoint = "/api/v1/ping"
url = base_url + endpoint

r = requests.get(url)

print(r.json())