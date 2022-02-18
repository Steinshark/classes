import os
import tensorflow as tf
import numpy as np
import math

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'



# Filters pq to only hold values that exist in the original ratings matrix
# Filter is in form:

#           [ 0  1  0  0  1 ]
#           [ 0  1  0  1  0 ]
#           [ 1  0  1  0  1 ]

# Where 1 held a rating in the original dataset
def map_to_existing(pq, filter):
    res = tf.math.multiply(pq,filter)
    input(res)
    return tf.math.multiply(pq,filter)


def GradientDescent(A,filter,dim=10,alpha=.1,iters=1000):

    # Ascertain what dimensions we are in
    cols    = A.shape[0]
    rows    = A.shape[1]

    # Create the P and Q matrices
    p       = tf.random.uniform(shape = [cols,dim],dtype=tf.dtypes.float32)
    q       = tf.random.uniform(shape = [dim,rows],dtype=tf.dtypes.float32)

    for i in range(iters):
        pq      = tf.matmul(p,q)
        A_pq   = tf.math.subtract(A,pq)

        # Calculate new p and q
        additional_p = tf.math.subtract(tf.transpose(q), A_pq) 
        new_p      = tf.math.add(p,    tf.math.multiply(    tf.math.multiply(  (2.0 * alpha), tf.transpose(q)),  A_pq))
        new_q      = tf.math.add(p,    tf.math.multiply(    tf.math.multiply(  (2.0 * alpha), tf.transpose(p)),  A_pq))

        p = new_p
        q = new_q

        input(RMSE(A,filter,p,q))
    return p_init,q_init

# A is assumed to be the Sparse Matrix of Ratings with many holes
def RMSE(A, filter,p,q):

    # 1 / T
    Tinv = tf.math.count_nonzero(filter,dtype=tf.dtypes.float32)

    # build pq with only elements that exist in A
    pq = map_to_existing(tf.matmul(p,q),filter)

    # Find distances squared from A
    A_pq = tf.math.subtract(A,pq)
    A_pq_square = tf.square(A_pq)

    # Find sum of distances
    sum = tf.reduce_sum(A_pq_square)

    # Return root of distances
    return math.sqrt(sum * Tinv)


if __name__ == "__main__":
    a = tf.constant([[1,2,3],[4,5,6]],dtype=tf.dtypes.float32)
    print(f"A:\n{a}\n\n")
    p,q = GradientDescent(a)
    err = RMSE(a,p,q)
    print({f"ERROR: {err}"})
