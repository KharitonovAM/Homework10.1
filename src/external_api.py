import json
import requests

with open('../.env') as f:
    my_api = json.load(f)['ApiKey']

def get_exchange(amount, frm):
    '''Принимает на вход сумму и валюту, возвращает сумму в рублях'''

    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={frm}&amount={amount}"
    payload = {}
    headers = {
        "apikey": my_api
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    repos = response.json()
    print(repos)
    return repos['result']
