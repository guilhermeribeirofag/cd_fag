import requests, json

url = "https://api.apilayer.com/exchangerates_data/latest"
resp = requests.get(url, params={"apikey":"Fim8F8Z6KttR6FbprwlNUkhuTabQ45NG", "base":"USD"})
data = resp.json()     # → dict!

print("EUR =", data["rates"]["EUR"])