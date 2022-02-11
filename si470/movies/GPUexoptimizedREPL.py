import tensorflow as tf
import pandas as pd
from os.path import join
import numpy as np
import os
import sys
from time import time
import pprint

HEADER = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
TAN = '\033[93m'
RED = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def printc(s,color,endl='\n'):
    print(f"{color}{s}{END}",end=endl,flush=True)

class Run:


    def __init__(self):
        self.this_movie = 0
        self.x = 0

    def euclidean_distance(self,A,B):
        subMatrix = A - B
        squareMatrix = tf.square(subMatrix)
        sumMatrix = tf.reduce_sum(squareMatrix)
        return tf.sqrt(sumMatrix)


    def slice_col_sparse(self,matrix,index):
        column_matrix_sparse    =  tf.sparse.slice(    matrix,     [0,index],     [matrix.shape[0],1])
        return tf.sparse.to_dense(column_matrix_sparse)
    def slice_row_sparse(self,matrix,index):
        row_matrix_sparse    =  tf.sparse.slice(    matrix,     [index,0],     [1,matrix.shape[1]])
        return                     tf.sparse.to_dense(row_matrix_sparse)

    def helper_func(self,dist):

        dist = tf.sparse.to_dense(dist)
        printc(f"I found {dist}",RED)
        dist = tf.reduce_sum(tf.square(dist - self.this_movie))
        self.x += 1
        printc(f"I was called",TAN)
        if dist < self.closest_movies[self.current_i]['distance'] and not self.x == self.current_i:
            printc(f"updated movie {self.current_i} to {self.x} dist {dist}",TAN)
            print(dist.numpy())
            self.closest_movies[self.current_i]['distance'] = dist.numpy()
            self.closest_movies[self.current_i]['movie']    = self.x

        printc(f"returning {dist}",TAN)
        return dist


    def run(self):
        user_liked = [0,1, 2, 5]
        self.closest_movies = {  movieId     :   {'movie' : 0, 'distance' : 10000} for movieId in user_liked}
        i64 = tf.dtypes.int64
        f64 = tf.dtypes.float64
        matrix = tf.sparse.reorder(tf.sparse.SparseTensor(indices = tf.constant([[0,0],[3,2],[4,1],[2,0],[5,1],[2,1]],dtype = i64),values = tf.constant([5,1,7,2,1.5,2]), dense_shape = [6,4]))

        for id in user_liked:
            printc(f"NEW USERS {id}\n\n",RED)
            self.current_i = id
            self.this_movie = self.slice_row_sparse(matrix,id)
            self.x = -1
            distances = tf.map_fn(  self.helper_func,
                                    matrix,
                                    dtype=tf.dtypes.float32)
        with open("output",'w') as file:
            file.write(pprint.pformat(self.closest_movies))
if __name__ == "__main__":
    r = Run()
    r.run()
