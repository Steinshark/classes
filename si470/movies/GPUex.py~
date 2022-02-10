import tensorflow as tf
import pandas as pd
from os.path import join
import numpy as np
import os
import sys
from time import time
# Package import to work on windows and linux
try:
    sys.path.append("C:\classes")
    sys.path.append("D:\classes")
    from Toolchain.terminal import *
except ModuleNotFoundError:
    sys.path.append("/home/m226252/classes")
    from Toolchain.terminal import *

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

t_32 = np.int64
t_64 = np.int64
f_16 = np.float16
df = pd.read_csv(datasets['large']['ratings'],sep = ',',dtype={'userId':t_32,'movieId':t_64,'rating':f_16})
printc(f"{df.head()}\n\n",TAN)

################################################################################
#                           Build Matrix indices and values
################################################################################
printc(f"Building Index and Value Tensors\n\n",GREEN)
t1 = time()
matrix_x = tf.convert_to_tensor(df['movieId'])
matrix_y = tf.convert_to_tensor(df['userId'])
index = tf.stack([matrix_x,matrix_y],axis=1)
value = tf.convert_to_tensor(df['rating'])
printc(f"Finished Tensor build in {(time()-t1):.3f} seconds",GREEN)
printc(f"\tindices: {index.shape}\n\tvalue: {value.shape}",GREEN)

matrix = tf.sparse.SparseTensor(indices=index,values=tf.transpose(value),dense_shape=[matrix_y.shape[0],matrix_x.shape[0]])
