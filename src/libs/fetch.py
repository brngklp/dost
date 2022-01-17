import requests
import json

def currencies(base: str, currency: str) -> str:
    #base = "usd"
    #currency = "try"
    host = f"https://api.coinbase.com/v2/prices/{base}-{currency}/spot"
    response = requests.get(host) 
    data = response.content.decode()
    parsed_data = json.loads(data)    
    amount = parsed_data["data"]["amount"]
    return f"1 {base.upper()} = {amount} {currency.upper()}"