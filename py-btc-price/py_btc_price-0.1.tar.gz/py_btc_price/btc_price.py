import requests

def get_btc_price(currency='USD'):
    response = requests.get('https://blockchain.info/ticker')
    
    if response.status_code == 200:
        return  response.json()[currency]['last']
