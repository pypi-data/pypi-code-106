import requests


def init(key):
    global seller
    seller=key
    pass

def create_key(days: int, level: int, amount: int):
    if days == None:
        print('Please provide a number of days for the key to be working.')
    elif level == None:
        level = 1
    elif amount == None:
        amount=1
    else:
        req = requests.get(f"https://keyauth.uk/api/seller/?sellerkey={seller}&type=add&expiry={days}&mask=XXXXXX-XXXXXX-XXXXXX-XXXXXX-XXXXXX-XXXXXX&level={level}&amount={amount}&format=json")
        reqj = req.json()
        result = reqj['key']
        othresult =reqj['keys']
        if reqj['success'] == True:
            if amount >= 2:
                return othresult
            else:
                return result
        else:
            print("Check your seller key.")
