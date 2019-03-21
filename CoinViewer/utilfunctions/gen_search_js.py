import json
import requests

url_usable = "https://api.coinmarketcap.com/v1/ticker/?start=0&limit=100"
response = requests.get(url_usable)
text = response.text
data = json.loads(text)

print("var names = [")
for coin in data:
    print("{")
    print("'url': '/coins/{}',".format(coin['symbol']))
    print("'label': '{} ({})',".format(coin['name'], coin['symbol']))
    print("'img_url': 'https://files.coinmarketcap.com/static/img/coins/32x32/{}.png',".format(coin['id']))
    print("},")
print("]")
