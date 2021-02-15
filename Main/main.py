from ReadFile.read import func_read
from FeatureSelection.REF.rfecv import func_rfeCV


x, y = func_read()
func_rfeCV(x, y)
