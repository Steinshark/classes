import tensorflow as tf
import pandas as pd
from os.path import join
import numpy as np
import os
import sys
from time import time
times = {'start' : time()}
# Package import to work on windows and linux
try:
    sys.path.append("C:\classes")
    sys.path.append("D:\classes")
    from Toolchain.terminal import *
    from Toolchain.DataTools import GPU_euclidean_dist
except ModuleNotFoundError:
    sys.path.append("/home/m226252/classes")
    from Toolchain.terminal import *


################################################################################
#                           Manage Logging
################################################################################
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
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


users = usna.values.tolist()



usna_movies_convert = [122906,96588,179819,175303,168326,177615,6539,79091,161644,115149,60397,192283,177593,8961]

usna_responses = {i : tf.convert_to_tensor([tf.constant([x,y],dtype=tf.dtypes.int64) for x,y in zip(usna_movies_convert,ratings)],dtype=tf.dtypes.int64) for i, ratings in enumerate(users)}
from pprint import pp
pp(usna_responses)
input()


################################################################################
#                           Get USNA Movies
###############################################################################




################################################################################
#                           Define a dictonary to map neighbors
###############################################################################





################################################################################
#                           Gather constants
################################################################################
#                                                   # dataset                           # column        #index
n_movies                            = int(  len(    dataframes['large']['movies']       ['movieId']                 ))
n_users                             = int(          dataframes['large']['ratings']      ['userId'].iloc      [-1]        )

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
input(matrix_x)
matrix_y = tf.convert_to_tensor(df['movieId'],dtype=tf.dtypes.int64)
index = tf.stack([matrix_x,matrix_y],axis=1)
input(index)
# Build value tensor
value = tf.convert_to_tensor(df['rating'],dtype=tf.dtypes.float16)
value = tf.transpose(value)

# Info
printc(f"Finished Tensor build in {(time()-t1):.3f} seconds",GREEN)
printc(f"\tindices: {index.shape}\n\tvalue: {value.shape}",GREEN)


################################################################################
#                           Build Sparse Matrix
################################################################################

matrix = tf.sparse.SparseTensor(indices=index,values=value,dense_shape=[matrix_y.shape[0],matrix_x.shape[0]])

################################################################################
#                           Define a dictonary to map neighbors
###############################################################################
movie = {
                movieId     :   0 for movieId in dataframes['large']['movies']
}

printc(f"{movie}",TAN)




################################################################################
#                           get slices
###############################################################################


for movieId in range(n_movies):
    column_matrix_sparse    =       tf.sparse.slice(    matrix,     [0,movieId],     [n_users,1])
    column_matrix           =       tf.sparse.to_dense(column_matrix_sparse)

    print(f"{euclidean_distance()}")
    printc(f"{column_matrix}",TAN)
