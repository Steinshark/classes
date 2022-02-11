import tensorflow as tf
import pandas as pd
from os.path import join
import numpy as np
import os
import sys
from time import time
import pprint

times = {'start' : time()}
# Package import to work on windows and linux
sys.path.append("C:\classes")
sys.path.append("D:\classes")
from Toolchain.terminal import *
from Toolchain.GPUTools import euclidean_distance, slice_col_sparse



################################################################################
#                           Manage Logging
################################################################################
printc(f"Num GPUs Available: {len(tf.config.list_physical_devices('GPU'))}\n\n",GREEN)
tf.debugging.set_log_device_placement(True)

################################################################################
#                           DATASET NAME DEFINITIONS
################################################################################

datasets = {    'small'     :  {'movies'        : join('ml-latest-small','movies.csv') , 'ratings' : join("ml-latest-small","ratings.csv") , 'tags' : join("ml-latest-small","tags.csv")},
                'large'     :  {'movies'        : join("ml-latest","movies.csv")       , 'ratings' : join("ml-latest","ratings.csv")       , 'tags' : join('ml-latest',"tags.csv")},
                'usna'      :  {'foodMovies'   : 'foodAndMovies.csv'}}

dataframes= {   'small'     :  {'movies'        : None, 'ratings' :  None, 'tags' : None},
                'large'     :  {'movies'        : None, 'ratings' :  None, 'tags' : None}}


headers = ["Black Panther","Pitch Perfect","Star Wars: The Last Jedi","It","The Big Sick","Lady Bird","Pirates of the Caribbean","Despicable Me","Coco","John Wick","Mamma Mia","Crazy Rich Asians","Three Billboards Outside Ebbings, Missouri","The Incredibles"]
################################################################################
#                           Read into DataFrame
################################################################################
printc(f"BEGIN: Data read from CSV",BLUE)
times['dread_s'] = time()
for size in datasets:
    for dset in datasets[size]:
        if not (size == 'large' and set == 'ratings') and not (size == 'usna' and dset == 'foodMovies'):
            printc(f"\treading {dset}-{size}",TAN,endl='')
            dataframes[size][dset]   = pd.read_csv(datasets[size][dset],sep=',')

            printc(f"\tsize: {(dataframes[size][dset].memory_usage().sum() / (1024.0*1024.0)):.2f} MB",TAN)

################################################################################
#                           Read into DataFrame
################################################################################

printc(f"\treading ratings-large",TAN)
f_64 = np.float64
df                                  = pd.read_csv(  datasets['large']['ratings'],   sep = ',',dtype={'userId':f_64,'movieId':f_64,'rating':f_64, 'timestamp':f_64})
usna                                = pd.read_csv(  datasets['usna']['foodMovies'],   sep = ',')
usna                                = usna[headers]
for col in headers:
    col_mean = usna[col].mean()
    usna[col].fillna(value=col_mean,inplace = True)

################################################################################
#                           Gather constants
################################################################################
#                                                   # dataset                           # column        #index
n_movies                            = int(  len(    dataframes['large']['movies']       ['movieId']                 ))
n_users                             = int(          dataframes['large']['ratings']      ['userId'].iloc      [-1]        )


################################################################################
#                           Convert USNA matrix to Workable Sparse Tensor
################################################################################

# Constant to have on hand
user_liked = [122906,96588,179819,175303,168326,177615,6539,79091,161644,115149,60397,192283,177593,8961]
#
## Split rows to lists (of ratings)
#users = usna.values.tolist()
#usna_matrices = []
#
## Fill
#for row in users:
#    vals = tf.convert_to_tensor(row,dtype=tf.dtypes.float16)
#    user_matrix = tf.sparse.SparseTensor(       indices = usna_movie_indexes,     values = vals,   dense_shape = [n_movies] )
#    usna_matrices.append(user_matrix)



################################################################################
#                           Get USNA Movies
###############################################################################




################################################################################
#                           Define a dictonary to map neighbors
###############################################################################


################################################################################
#                           Show Data
################################################################################

printc(f"\n\nDATASET: ",BLUE)
printc(f"\t{BLUE}'ratings' looks like:  {END}\n     {df.head(3)}\n\n",TAN)
printc(f"\t{BLUE}'movies' looks like:   {END}\n     {dataframes['large']['movies'].head(3)}\n\n",TAN)

printc(f"\t{BLUE}number of users:       {END}       {n_users}",TAN)
printc(f"\t{BLUE}number of movies:      {END}       {n_movies}\n\n",TAN)

################################################################################
#                           Build Matrix indices and values
################################################################################

printc(f"Building Index and Value Tensors\n\n",GREEN)
t1 = time()
# Set x,y index arrays and build index tensor (2,x)
matrix_x = tf.convert_to_tensor(df['userId'],dtype=tf.dtypes.int64)
matrix_y = tf.convert_to_tensor(df['movieId'],dtype=tf.dtypes.int64)
index = tf.stack([matrix_x,matrix_y],axis=1)
# Build value tensor
value = tf.convert_to_tensor(df['rating'],dtype=tf.dtypes.float64)
value = tf.transpose(value)

# Info
printc(f"Finished Tensor build in\t{(time()-t1):.3f} seconds",GREEN)
printc(f"\tindices:\t{index.shape}\n\tvalue: {value.shape}",GREEN)


################################################################################
#                           Build Sparse Matrix
################################################################################

matrix = tf.sparse.SparseTensor(indices=index,values=value,dense_shape=[matrix_y.shape[0],matrix_x.shape[0]])

################################################################################
#                           Define a dictonary to map neighbors
###############################################################################
closest_movies = {
                movieId     :   {'movie' : 0, 'distance' : 10000} for movieId in user_liked
}



def helper_func(dist,current_i):
    global x
    x += 1

    if dist < closest_movies[i]['distance'] and not x == current_i:
        printc(f"updated movie {current_i} to {x} dist {dist}")
        closest_movies[i]['distance'] = dist
        closest_movies[i]['movie']    = x





################################################################################
#                           get slices
###############################################################################

for id in user_liked:
    # The movie we know we like
    this_movie = slice_col_sparse(matrix,id)

    x = 0
    distances = tf.map_fn(lambda A :  helper_func(tf.reduce_sum(tf.square(A - this_movie)), id), matrix, dtype=tf.dtypes.float64)

with open("output",'w') as file:
    file.write(pprint.pformat(closest_movies))
