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

def classify(dataPath,categoryPath):
  statement=pd.read_csv(dataPath)
  statement=statement[statement.Amount<0]
  statement['Category']='None'
#print(statement)
  keywords=pd.read_csv(categoryPath,index_col=0,header=None).T.stack()
  keywords.index=keywords.index.droplevel(None)
  keywords=keywords.sortlevel()
  for category,keyword in keywords.iteritems():
    statement.Category=statement.apply(lambda i:categorySet(i.Category,i.Description,category,keyword),axis=1)
  return statement

# CATEGORIZE STATEMENT
#statement=classify("../finances/stmt.csv","categories.csv")
#statement[statement['Category']=='None'].to_csv("../finances/unclassified.csv",index=None)
#statement.to_csv("../finances/classified.csv",index=None)


statement=pd.read_csv("../finances/classified.csv")
categories=statement.groupby('Category').sum()
#print(statement[statement.Category=='Money Transfer'])
print(categories.sort_values(by='Amount'))
print(statement[statement.Category=='Money Transfer'])

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
