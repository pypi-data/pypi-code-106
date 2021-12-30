import requests

def get_btc_price(currency='USD'):
    response = requests.get('https://blockchain.info/ticker')
    
    if response.status_code == 200:
        return  response.json()[currency]['last']
    
    return None
    

def usd_convert(amount):
    try:
        current_price = get_btc_price('USD')
        
        if current_price:
            return (1.0 / current_price ) * amount
        
    except Exception as err:
        
        return None
