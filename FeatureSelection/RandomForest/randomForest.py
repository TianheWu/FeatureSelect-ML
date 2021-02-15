from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import pandas as pd


def func_randomForest(x, y):
    model = RandomForestRegressor()
    model.fit(x, y)
    print(model.feature_importances_)
    f_importance = pd.Series(model.feature_importances_, index=x.columns)
    f_importance.nlargest(10).plot(kind='barh')
    plt.show()
