import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

class ML:

    def __init__(self):
        dataset = pd.read_csv("./data.csv")
        X = []
        for item in dataset['data']:
            X.append([int(item)])
        y = []
        for item in dataset['target']:
            y.append(int(item))
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01)
        model = LinearRegression()
        model.fit(X_train, y_train)
        self.model = model
        self.mae = mean_absolute_error(y_test, model.predict(X_test))

    def predict(self, light):
        x = [[light]]
        return int(self.model.predict(x))