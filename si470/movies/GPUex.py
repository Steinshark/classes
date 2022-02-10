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

datasets = {    'small'     :  {'movies' : join('ml-latest-small','movies.csv') , 'ratings' : join("ml-latest-small","ratings.csv") , 'tags' : join("ml-latest-small","tags.csv")},
                'large'     :  {'movies' : join("ml-latest","movies.csv")       , 'ratings' : join("ml-latest","ratings.csv")       , 'tags' : join('ml-latest',"tags.csv")}}

dataframes= {   'small'     :  {'movies' : None, 'ratings' :  None, 'tags' : None},
                'large'     :  {'movies' : None, 'ratings' :  None, 'tags' : None}}

################################################################################
#                           Read into DataFrame
################################################################################
printc(f"BEGIN: Data read from CSV",BLUE)
times['dread_s'] = time()
for size in datasets:
    for dset in datasets[size]:
        if not (size == 'large' and set == 'ratings'):
            printc(f"\treading {dset}-{size}",TAN)
            dataframes[size][dset]   = pd.read_csv(datasets[size][dset],sep=',')

################################################################################
#                           Read into DataFrame
################################################################################
printc(f"\treading ratings-large",TAN)

t_32 = np.int64
t_64 = np.int64
f_16 = np.float16
df                                  = pd.read_csv(  datasets['large']['ratings'],   sep = ',',dtype={'userId':t_32,'movieId':t_64,'rating':f_16})

printc(f"Finished Data read in {time()-times['dread_s']:.3f} seconds",GREEN)
################################################################################
#                           Gather constants
################################################################################

n_movies                            = int(  len(    dataframes['large']['movies']       ['movieId'] ))
n_users                             = int(          dataframes['large']['ratings']      ['userId']  [-1]        )

################################################################################
#                           Show Data
################################################################################

printc(f"DATASET: ")
printc(f"\t'ratings' looks like:\n{df.head(3)}...\n{df.tail(3)}\n\n",TAN)
printc(f"\t'movies' looks like:\n{dataframes['large']['movies'].head(3)}...\n{dataframes['large']['movies'].tail(3)}\n\n",TAN)

printc(f"\tnumber of users: {n_users}",TAN)
printc(f"\tnumber of movies: {n_movies}\n\n",TAN)

################################################################################
#                           Build Matrix indices and values
################################################################################

printc(f"Building Index and Value Tensors\n\n",GREEN)
t1 = time()
# Set x,y index arrays and build index tensor (2,x)
matrix_x = tf.convert_to_tensor(df['movieId'])
matrix_y = tf.convert_to_tensor(df['userId'])
index = tf.stack([matrix_x,matrix_y],axis=1)


# Build value tensor
value = tf.convert_to_tensor(df['rating'])
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


for column in n_movies:
    printc(f"{tf[:,column]}",TAN)
