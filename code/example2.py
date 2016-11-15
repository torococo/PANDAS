import pandas as pd

pieces = [];
for year in range(1880, 2011):
  pieces.append(pd.read_csv("../data/ch02/names/yob1880.txt", names=['name','sex','births']))

names=pd.concat(pieces,ignore_index=True)
print(names)
