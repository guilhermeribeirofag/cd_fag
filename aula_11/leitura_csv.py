import csv, statistics as st

with open("../aula_05/Sales_April_2019.csv", newline="") as f:
    leitor = csv.DictReader(f, delimiter=",", skipinitialspace=True)
    precos = [float(l["Price Each"] or 0) for i, l in enumerate(leitor) if l["Price Each"].strip()]

print("Ticket médio:", st.mean(precos))