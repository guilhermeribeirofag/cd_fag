import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, None, 4],
    "B": [3, 4, 5, 6]
})

df["A_filled"] = df["A"].fillna(df["A"].median())
resultado = df["A_filled"].mean()
print(resultado)
