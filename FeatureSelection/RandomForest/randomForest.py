from sklearn.ensemble import RandomForestRegressor


def func_randomForest(x, y):
    model = RandomForestRegressor()
    model.fit(x, y)
    return model
