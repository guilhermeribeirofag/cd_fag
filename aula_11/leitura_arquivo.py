with open("notas.txt", "r", encoding="utf-8") as f:
    linhas = [l.strip() for l in f]
    print(linhas)

# with open("resultado.txt", "w") as g:
#     g.write("\n".join(linhas))

import pandas as pd

df = pd.DataFrame({'nota': linhas})
df['ordem_notas'] = df.index
df['ordem_notas'] = df['ordem_notas'] + 1

print(0)