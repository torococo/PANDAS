import numpy as np
from numba import njit

x=np.array(["this","is","a","test"],'S4')
y=np.array(["1",2,3,4,5,6],'i').reshape(3,2)
print(y.cumsum(0))


@njit
def numbaTest(x):
  return x+5

print(numbaTest(10))
