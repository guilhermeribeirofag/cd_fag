import pandas as pd

# Exercício 1: 5 maiores médias de ataque por geração
df = pd.read_csv(r'D:\Mega\FAG\fag_projects\aula_11\pokemon.csv')
df_final = df.groupby(['GENERATION']).mean()['ATK'].sort_values(ascending=False).head(5)
print(df_final)


# Exercício 2: pokemons que possuem velocidade de ataque maior que 50
df_sp_atk = df[df['SP_ATK'] > 50]
print(df_sp_atk)