import re
import requests
import json

# реалізація логику запитів курсу валют.
# PrivatBank API.
# URL: https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5.
URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
# Приклад відповіді:
# {'ccy': 'USD', 'base_ccy': 'UAH', 'buy': '36.75000', 'sale': '37.25000'}

def load_exchange():
    return json.loads(requests.get(URL).text)

def get_exchange(ccy_key):
    for exc in load_exchange():
        if ccy_key == exc['ccy']:
            return exc
    return False

def get_exchanges(ccy_pattern):
    result = []
    ccy_pattern = re.escape(ccy_pattern) + '.*'
    for exc in load_exchange():
        if re.match(ccy_pattern, exc['ccy'], re.IGNORECASE) is not None:
            result.append(exc)
    return result
exchange_now = get_exchange("USD")
print(exchange_now) # {'ccy': 'USD', 'base_ccy': 'UAH', 'buy': '26.70000', 'sale': '27.10000'}
