import requests, time
from bs4 import BeautifulSoup

URL = "https://globo.com"
titulos = []

for page in range(1):
    resp = requests.get(URL.format(page), timeout=10)
    if resp.status_code != 200:
        print("falha", page);  continue

    soup = BeautifulSoup(resp.text, "html5lib")
    for h2 in soup.find_all("h2"):
        print(h2)
        titulos.append(h2.get_text(strip=True))

    time.sleep(3)  # politeness (robots.txt pede 3 s)
print(len(titulos), "posts coletados")