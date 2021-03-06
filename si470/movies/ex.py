import sys
import pandas as pd
import numpy as np

from time import time
from os.path import join
from scipy.sparse import coo_matrix

from sklearn.neighbors import NearestNeighbors

################################################################################
#                           DATASET NAME DEFINITIONS
################################################################################

datasets = {    'small'     :  {'movies' : join('ml-latest-small','movies.csv') , 'ratings' : join("ml-latest-small","ratings.csv") , 'tags' : join("ml-latest-small","tags.csv")},
                'large'     :  {'movies' : join("ml-latest","movies.csv")       , 'ratings' : join("ml-latest","ratings.csv")       , 'tags' : join('ml-latest',"tags.csv")}}

dataframes= {   'small'     :  {'movies' : None, 'ratings' :  None, 'tags' : None},
                'large'     :  {'movies' : None, 'ratings' :  None, 'tags' : None}}


################################################################################
#                           READ IN DATASETS
#           ASSUMPTION TO BE MADE HERE: how do we fill the na?
#           Since we are using a sparse matrix, the values will be 0
################################################################################

t1 = time()
for size in dataframes:
    for mtype in dataframes[size]:
        dataframes[size][mtype] = pd.read_csv(datasets[size][mtype],sep=',')

################################################################################
#                           GET DATA SHAPE
################################################################################

n_movies = dataframes['large']['movies']['movieId'].iloc[-1]
n_users  = dataframes['large']['ratings']['userId'].iloc[-1]

print(f"shape: {n_movies,n_movies}")

################################################################################
#                        INIT MATRIX FOR READ
################################################################################

#lil_matr = lil_matrix((n_users,n_movies))
#file = open(datasets['large']['ratings'])
#file.readline()# Remove fields from top of file



################################################################################
#                        READ FILE
################################################################################
#for line in file:
#    userId, movieId, ratingId, timestamp = line.split(',')
#    lil_matr[int(userId),int(movieId)] = float(ratingId)

################################################################################
#                        INIT MATRIX FOR READ
################################################################################
matrix = coo_matrix( (dataframes['large']['ratings']['rating'],(dataframes['large']['ratings']['movieId'],dataframes['large']['ratings']['userId'])))



print(f"\tsize: {matrix.data.size/(1024**2):.2f} MB")
print(f'finished in {time()-t1} seconds')


t2 = time()
model = NearestNeighbors(n_neighbors=10)
t2 = time()
print("fitting data")
model.fit(matrix)
print(f"fit in {(time()-t2):.3f} seconds")
