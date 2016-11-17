import pandas as pd
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt


def categorySet(currCat,description,newCat,keyWord):
  if keyWord in description:
    if currCat!='None' and currCat!=newCat:
      raise ValueError('"'+description+'"'+'fits in 2 categories: ['+currCat+','+newCat+'] triggered by keyword: '+'"'+keyWord+'"')
    return newCat
  return currCat

statement=pd.read_csv("../finances/stmt.csv")
statement['Category']='None'
#print(statement)
keywords=pd.read_csv("categories.csv",index_col=0,header=None).T.stack()
keywords.index=keywords.index.droplevel(None)
keywords=keywords.sortlevel()
for category,keyword in keywords.iteritems():
  statement.Category=statement.apply(lambda i:categorySet(i.Category,i.Description,category,keyword),axis=1)

#for cat in categories.columns:
#  for entry in categories[cat]:
#    if not pd.isnull(entry):
#
classified=statement[statement.Category!='None']
unclassified=statement[statement.Category=='None']
unclassified.to_csv("../finances/unclassified.csv",index=False)
print(statement[statement.Category=='None'].shape[0])
print(statement[statement.Category!='None'].shape[0])

#classifiers.to_csv("test.csv")
#classifier=buyClassifier()
#for line in classifiers:
#  classifier.AddIDs(line[0],*line[1:])
#mask=classifier.UnclassifiedMask(statement.Description)
#print(mask.sum())
#unclassified=statement[mask]
#print(statement.shape[0])
#print(unclassified.shape[0])
#unclassified.to_csv("../finances/unclassified.csv",index=False)
#print(classifier.SubTable('Dining',statement,statement.Description))














#print(statement.columns)
#print(mask)
#print(statement.shape)
#mask=statement.Description.str.contains('FOOD');
#print(statement[statement.Description.str.contains('FOOD')]);
#pd.to_numeric(statement['Date'])
#print(statement.stack().swaplevel(0,1).sortlevel(0))
#print(statement.Description.value_counts())
#plt.show()
