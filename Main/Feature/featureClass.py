from ReadFile.read import func_read
from FeatureSelection.RandomForest.randomForest import func_randomForest
from InquireMiRNA.buildDict import func_buildDict
import matplotlib.pyplot as plt
import pandas as pd


class Feature:

    def __init__(self, n):
        self.x, self.y = func_read()
        self.mirna_n, self.n_mirna = func_buildDict(self.x)
        self.selectedNum = n
        self.model = func_randomForest(self.x, self.y)

    def getImportance(self):
        return self.model.feature_importances_

    def printFI(self):
        print(self.model.feature_importances_)

    def draw(self):
        f_importance = pd.Series(self.model.feature_importances_, index=self.x.columns)
        f_importance.nlargest(self.selectedNum).plot(kind='barh')
        plt.show()





