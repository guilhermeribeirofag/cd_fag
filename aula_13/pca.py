from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd

df = pd.read_csv("WineQT.csv", sep=",")
X  = StandardScaler().fit_transform(df.drop("quality", axis=1))

pca = PCA().fit(X)                 # ajusta em todas as comp.


import matplotlib.pyplot as plt
plt.plot(range(1, 13), pca.explained_variance_ratio_.cumsum(), marker="o")
plt.xlabel("nº componentes"); plt.ylabel("var. acumulada"); plt.grid()

print('')

Z2 = PCA(n_components=4).fit_transform(X)
plt.scatter(Z2[:,0], Z2[:,1], c=df["quality"], cmap="coolwarm", s=15)
plt.colorbar(label="quality score"); plt.title("Wine PCA 2-D")

plt.show()