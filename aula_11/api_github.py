import requests
from collections import Counter

BASE = "https://api.github.com/users/{user}/repos"
def year_hist(user):
    repos = requests.get(BASE.format(user=user),
                         params={"per_page": 100}).json()
    anos = [int(r["created_at"][:4]) for r in repos]
    return Counter(anos)

hist = year_hist("pallets")     # criadores do Flask
print(hist.most_common())