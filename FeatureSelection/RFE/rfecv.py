from sklearn.model_selection import KFold
from sklearn.feature_selection import RFECV
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt


def func_rfecv(x, y):

    rfr = RandomForestRegressor()
    rfecv = RFECV(estimator=rfr, cv=KFold(n_splits=3, random_state=2), scoring='neg_mean_squared_error')
    rfecv.fit(x, y)
    print(rfecv.n_features_)
    print(rfecv.ranking_)
    # plt.figure()
    # plt.xlabel("Number of features selected")
    # plt.ylabel("Cross validation score (nb of correct classifications)")
    # plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
    # plt.show()
    return rfecv.ranking_