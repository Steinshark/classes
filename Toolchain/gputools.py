################################################################################
#                           IMPORTS
################################################################################
from tensorflow import square, reduce_sum, sqrt, sparse
from tensorflow.sparse import to_dense
from .terminal import *

# Computes the euclidean distance of tensors A and B
def euclidean_distance(A,B):

    # Error Check
    if not A.shape == B.shape:
        printc(f"\tshape mismatch A: {A.shape}, B: {B.shape}",RED)
        return

    #ALGORITHM

    # 1 - Calc pointwise difference
    subMatrix = A - B

    # 2 - Find square of distance
    squareMatrix = tf.square(subMatrix)

    # 3 = Find the sum of the square distance
    sumMatrix = tf.reduce_sum(squareMatrix)

    # 4 - return the squareroot of the sumMatrix
    return tf.sqrt(sumMatrix)

def slice_col_sparse(matrix,index):
    return  slice(    matrix,     [0,index],     [matrix.shape[0],1])
    return                          to_dense(column_matrix_sparse)
