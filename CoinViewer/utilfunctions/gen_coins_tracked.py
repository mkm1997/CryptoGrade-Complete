import json
import requests

url_usable = "https://api.coinmarketcap.com/v1/ticker/?start=0&limit=100"
response = requests.get(url_usable)
text = response.text
data = json.loads(text)

print("coins_tracked = [")
for coin in data:
    print("    '" + coin['symbol'] + "',")
print("]")

