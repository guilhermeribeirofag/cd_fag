import pandas as pd
import requests
import json

URL = "https://pokeapi.co/api/v2/pokemon/"

response = requests.get(URL, timeout=10)

if response.status_code == 200:
    resposta = response.json()
    df = pd.DataFrame(resposta['results'])
    df = df.head(10)

    for indice, linha in df.iterrows():
        resp_poke = requests.get(linha['url'], timeout=10)
        json_poke = resp_poke.json()
        print(linha['name'] + " " + str(json_poke['height']))
        print(linha['name'] + " " + str(json_poke['weight']))
else:
    print('Problemas ao buscar Pokemons para análise')
