from sklearn.linear_model import Ridge
from sklearn.feature_selection import RFE


def func_rfe(x, y):
    lr = Ridge(alpha=100000, fit_intercept=True, normalize=True,
               copy_X=True, max_iter=1500, tol=1e-4, solver='auto')

    rfe = RFE(estimator=lr, n_features_to_select=10)
    rfe.fit(x, y)

    # print("Num Features: " + str(rfe.n_features_))
    # print("Selected Features: " + str(rfe.support_))
    # print("Feature Ranking: " + str(rfe.ranking_))

    return rfe.ranking_
