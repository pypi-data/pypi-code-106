import requests
import json

sellerkey2=None

def init(sellerkey):
    global sellerkey2
    sellerkey=sellerkey2

def create_key(days, level, amount):
    if days == None:
        print('Please provide a number of days for the key to be working.')
    if level == None:
        level = 1
    if amount == None:
        amount=1
        req = requests.get(f"https://keyauth.com/api/seller/?sellerkey={sellerkey2}&type=add&expiry={days}&mask=XXXXXX-XXXXXX-XXXXXX-XXXXXX-XXXXXX-XXXXXX&level={level}&amount={amount}&format=json")
        reqj = req.json()
        key = reqj['key']
        if reqj['success'] == True:
            return reqj['key']