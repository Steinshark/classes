import tensorflow as tf
import pandas as pd
import numpy as np
import os
import Algorithms
from terminal import *
from time import time

tf.config.run_functions_eagerly(True)

#TYPES
_f32            = tf.dtypes.float32
_i32            = tf.dtypes.int32
#DATASET LOCATIONS
_RATINGS_SMALL  = os.path.join("ml-latest-small","ratings.csv")
_MOVIE_ID_SMALL = os.path.join("ml-latest-small","movies.csv")
_HEADERS        = ["Black Panther",
                   "Pitch Perfect",
                   "Star Wars: The Last Jedi",
                   "It",
                   "The Big Sick",
                   "Lady Bird",
                   "Pirates of the Caribbean",
                   "Despicable Me",
                   "Coco",
                   "John Wick",
                   "Mamma Mia",
                   "Crazy Rich Asians",
                   "Three Billboards Outside Ebbings, Missouri",
                   "The Incredibles"]

_MOVIE_ID_MAP      = {}
_ROW_MAP           = {}


def fill(df,method):
    for col in df:
        if method == 'mean':
            replacement = df[col].mean()
        elif method   == 'zero':
            replacement = 0
        df[col].fillna(value = replacement, inplace = True)


def read_data():
    printc(f"\tReading data",BLUE)
    t1 = time()

    # Read 'ratings.csv' into a DataFrame from the small set
    small_ratings   = pd.read_csv(  _RATINGS_SMALL,
                                    dtype = {   'userId'    :   np.float32,
                                                'movieId'   :   np.float32,
                                                'rating'    :   np.float32,
                                                'timestamp' :   np.float32})

    small_movie_ids  = pd.read_csv(  _MOVIE_ID_SMALL,
                                    dtype = {   'movieId' : np.float32})

    # Convert the dataframe to correct matrix format: (rows=MovieId, cols=userId)
    small_ratings_matrix = small_ratings.pivot( index='movieId',    columns='userId',   values='rating')

    # Map movieId to row and vice versa
    for row, id in enumerate(small_movie_ids['movieId']):
        _MOVIE_ID_MAP[row]  = id
        _ROW_MAP[id]        = row
    #info
    # Fill with our choice
    fill(small_ratings_matrix,'zero')

    # convert the dataframe to a Tensor
    partial_ratings_tensor  = tf.convert_to_tensor(  small_ratings_matrix,   dtype = _f32)

    # convert all non_zero elements to 1
    partial_ratings_filter  = tf.sparse.to_dense(tf.sparse.map_values(tf.ones_like,tf.sparse.from_dense(partial_ratings_tensor)))
    partial_ratings_filter  = tf.cast(partial_ratings_filter, dtype=_f32)

    printc(f"\tRead data in {(time()-t1):.3f} seconds",GREEN)
    return partial_ratings_tensor, partial_ratings_filter

ratings, filter_matrix = read_data()

alphas = [1,.5,.1,.01] 
iter_val = np.arange(0,10000,2000)



runs = {a : { test : [] for test in iter_val } for a in alphas}
colors = {1 : 'b',.5 : 'g',.1 : 'r',.01 : 'm' }


for a in alphas:
    for test_val in iter_val:

        t1 = time()
        p,q = Algorithms.GradientDescent_optimized(ratings,filter_matrix,dim=7,iters=test_val,alpha = a)
        runs[a][test_val].append(time()-t1)
        runs[a][test_val].append(Algorithms.RMSE(ratings,filter_matrix,p,q))

from matplotlib import pyplot as plt 


fix, ax = plt.subplots(len(alphas))

for i,a in enumerate(runs):
    for x in runs[a]:
        ax[i].scatter(x,times[a], color=colors[a])
        ax[i].scatter(x,rmses[a], color=colors[a])
plt.show()
