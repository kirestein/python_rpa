import requests

link_usd = 'https://economia.awesomeapi.com.br/last/USD'
link_eur = 'https://economia.awesomeapi.com.br/last/EUR-BRL'

req_usd = requests.get(link_usd)
req_eur = requests.get(link_eur)

value_usd = req_usd.json()['USDBRL']['high']
value_eur = req_eur.json()['EURBRL']['high']


print(f'{value_usd=}')
print(f'{value_eur=}')
