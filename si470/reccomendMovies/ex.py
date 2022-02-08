import pandas as pd
import numpy as np
from scipy.sparse import lil_matrix
from time import time

#init all of the filenames and dataframes
datasets = {    'small'     :  {'movies' : "ml-latest-small/movies.csv" , 'ratings' : "ml-latest-small/ratings.csv" , 'tags' : "ml-latest-small/tags.csv"},
                'large'     :  {'movies' : "ml-latest/movies.csv"       , 'ratings' : "ml-latest/ratings.csv"       , 'tags' : "ml-latest/tags.csv"}}
dataframes= {   'small'     :  {'movies' : None, 'ratings' :  None, 'tags' : None},
                'large'     :  {'movies' : None, 'ratings' :  None, 'tags' : None}}

# read in the datasets
# ASSUMPTION TO BE MADE HERE: how do we fill the na?
# We choprint(f"\tsize: {lil_matr.data.size/(1024**2):.2f} MB")
t1 = time()
for size in dataframes:
    for type in dataframes[size]:
        dataframes[size][type] = pd.read_csv(datasets[size][type],sep=',')

n_movies = dataframes['large']['movies']['movieId'].iloc[-1]
n_users  = dataframes['large']['ratings']['userId'].iloc[-1]

print(f"shape: {n_users,n_movies}")

lil_matr = lil_matrix((n_users+1,n_movies+1))
file = open(datasets['large']['ratings'])
file.readline()

for line in file:
    userId, movieId, ratingId, timestamp = line.split(',')
    lil_matr[int(userId),int(movieId)] = float(ratingId)



#for i in range(len(dataframes['large']['ratings'])):
#    userId  = dataframes['large']['ratings']['userId'][i]
#    movieId = dataframes['large']['ratings']['movieId'][i]
#    ratingId = dataframes['large']['ratings']['rating'][i]
#    lil_matr[userId,movieId] = ratingId
print(f"\tsize: {lil_matr.data.size/(1024**2):.2f} MB")
print(f'finished in {time()-t1} seconds')



#small_1 = dataframes['large']['ratings'][dataframes['large']['ratings']['userId'] == 1].pivot(index='userId',columns='movieId')
#print(small_1.to_numpy((1,n_movies)))
#print(small_l.shape)
#input()
#splits = [ dataframes['large']['ratings'][dataframes['large']['ratings']['userId'] == i] for i in range(dataframes['large']['ratings']['userId'].iloc[-1])]


#print(splits)


#for line in dataframes['large']['ratings'].loc[:, ['userId','movieId']]:
#    print( type( dataframes['large']['ratings'][line]  ))
