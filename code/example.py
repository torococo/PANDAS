import json
from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt

x=pd.DataFrame([[6,2,3],[4,5,1]],columns=['b','c','a'])
print(x.quantile([0.25,0.5,0.75]))

#def readJson(path):
#  return [json.loads(line) for line in open(path)]


# listOfDicts=readJson("./data/ch02/usagov_bitly_data2012-03-16-1331923249.txt")
# print listOfDicts[0]['tz']
# timeZones=[rec['tz']for rec in listOfDicts if 'tz' in rec]
# print timeZones

# frame=DataFrame(listOfDicts)
# frame['tz'].value_counts()[:10].plot(kind='barh',rot=0)
# plt.show()

#unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
#users = pd.read_table('../data/ch02/movielens/users.dat', sep='::', header=None, names=unames)
#rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
#ratings = pd.read_table('../data/ch02/movielens/ratings.dat', sep='::', header=None, names=rnames)
#mnames = ['movie_id', 'title', 'genres']
#movies = pd.read_table('../data/ch02/movielens/movies.dat', sep='::', header=None, names=mnames)
#data = pd.merge(pd.merge(ratings, users), movies)
#
#mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
#mean_ratings['diff'] = mean_ratings['M']-mean_ratings['F']
#sorted_by_diff = mean_ratings.sort_index(by='diff')

#print(sorted_by_diff[::-1][:15])

# print(mean_ratings[:5])
