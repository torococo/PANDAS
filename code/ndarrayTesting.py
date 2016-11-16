#import numpy as np
import pandas as pd
#from numba import njit

#x=np.array(["this","is","a","test"],'S4')
#y=np.array(["1",2,3,4,5,6],'i').reshape(3,2)
#print(y.cumsum(0))
#
#
#@njit
#def numbaTest(x):
#  return x+5

#print(numbaTest(10))

a=pd.Series(['a','b','c'],[1,2,3])
b=pd.Series(['d','e','f'],[1,2,3])
x=pd.DataFrame({'1':a,'2':b})
print(x)

#x=pd.DataFrame([[1,2,3],[4,5,6]],index=['a','b'],columns=['i','j','k'])
#y=x.T
#print(y.ix[0])
