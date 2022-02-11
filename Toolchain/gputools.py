################################################################################
#                           IMPORTS
################################################################################
import tensorflow as tf
from .terminal import *

# Computes the euclidean distance of tensors A and B
@tf.function
def euclidean_distance(A,B):
    # 4 - return the squareroot of the sumMatrix
    return tf.norm(A-B,ord='euclidean')

def slice_col_sparse(matrix,index):
    column_matrix_sparse    =   tf.sparse.slice(    matrix,     [0,index],     [matrix.shape[0],1])
    return                      tf.sparse.to_dense(column_matrix_sparse)

def slice_row_sparse(matrix,index):
    row_matrix_sparse       =  tf.sparse.reorder( tf.sparse.slice(    matrix,     [index,0],     [1,matrix.shape[1]]))
    return                     tf.sparse.to_dense(row_matrix_sparse)
