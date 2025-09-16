from collections import Counter
import math

def euclid(a, b):
    return math.sqrt(sum((xi - yi)**2 for xi, yi in zip(a, b)))

def majority_vote(labels):
    counts = Counter(labels)
    top, freq = counts.most_common(1)[0]
    if list(counts.values()).count(freq) == 1:
        return top               # vencedor único
    return majority_vote(labels[:-1])  # desempate recursivo

def knn_classify(k, labeled_points, x_new):
    # labeled_points: list[(vector, label)]
    by_dist = sorted(labeled_points, key=lambda p: euclid(p[0], x_new))
    k_labels = [label for _, label in by_dist[:k]]
    return majority_vote(k_labels)


from sklearn.datasets import load_wine

X, y = load_wine(return_X_y=True, as_frame=True)

# lista de (vetor, rótulo)
labeled_points = list(zip(X.values, y.values))

# amostra que queremos classificar (linha 0)
x_new = X.iloc[120].values

print(knn_classify(3, labeled_points, x_new))  # deve imprimir 0, 1 ou 2