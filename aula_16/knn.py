from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, train_test_split

X, y = load_wine(return_X_y=True, as_frame=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)
grid = GridSearchCV(KNeighborsClassifier(),
                    param_grid={'n_neighbors':[1,3,5,7,9]})
grid.fit(X_train, y_train)
print("Best k:", grid.best_params_['n_neighbors'],
      "  Acc =", grid.score(X_test, y_test))