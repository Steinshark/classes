import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import numpy as np
import math




def map_to_missing(holes, full):
    d = tf.sparse.map_values(tf.ones_like,s)


def GradientDescent(real_data,alpha=.1,iters=1000):

    # Ascertain what dimensions we are in
    cols    = real_data.shape[0]
    rows    = real_data.shape[1]

    # Create the P and Q matrices
    dim = 3
    p_init   = tf.random.uniform(shape = [cols,dim],dtype=tf.dtypes.float32)
    q_init   = tf.random.uniform(shape = [dim,rows],dtype=tf.dtypes.float32)
    return p_init,q_init

# A is assumed to be the Sparse Matrix of Ratings with many holes
def RMSE(A,p,q):
#       sqrt( (1 / T)*(sum(A_ij - (p_i)(q_j))^2) )
    # 1 / T
    Tinv = tf.constant(1 / tf.math.count_nonzero(A),dtype=tf.dtypes.float32)

    #
    pq = tf.matmul(p,q)
    A_pq = tf.math.subtract(A,pq)
    A_pq_square = tf.square(A_pq)

    # Dont incldue blank indices 'Frobenius norm '
    sum = tf.reduce_sum(A_pq_square)


    return math.sqrt(sum * Tinv)


if __name__ == "__main__":
    a = tf.constant([[1,2,3],[4,5,6]],dtype=tf.dtypes.float32)
    print(f"A:\n{a}\n\n")
    p,q = GradientDescent(a)
    err = RMSE(a,p,q)
    print({f"ERROR: {err}"})
