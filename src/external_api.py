import json
import os
from dotenv import load_dotenv
import requests

def get_exchange(amount, frm):
    '''Принимает на вход сумму и валюту, возвращает сумму в рублях'''

    load_dotenv()
    my_api = os.getenv('ApiKey')
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={frm}&amount={amount}"
    payload = {}
    headers = {
        "apikey": my_api
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    repos = response.json()
    return repos['result']
