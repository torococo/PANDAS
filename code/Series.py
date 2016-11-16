import numpy as np
import pandas as pd

ex=pd.Series([4,3,6,-1],['a','b','c','d'])
#ex.index=np.array(['a','b','c','d'],'S1')
ex2=pd.Series(ex,['b','e'])
print(ex.a)
