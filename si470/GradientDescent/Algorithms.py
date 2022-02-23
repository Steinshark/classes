import os
import tensorflow as tf
import numpy as np
import math
from time import time
from terminal import *

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def map_to_existing(pq, filter):
    res = tf.math.multiply(pq,filter)
    return tf.math.multiply(pq,filter)


def GradientDescent(A,p,q,filter_matrix,dim=10,alpha=.1,iters=1):
    printc(f"\tentered GradientDescent algorithm",TAN)

    const   = alpha * 2.0
    for iter in range(iters):


        for j in range(cols):
            t1 = time()
            printc(f"\t\tstart col {j}",TAN,endl='')
            for i in range(rows):
                if not filter[i][j]:
                    continue
                # get q col and p row
                q_j = q[:,j]
                p_i = p[i]


                # find the err present
                err = tf.math.subtract(A[i][j],tf.math.multiply(q_j, p_i))

                # find where to nudge down the gradient
                nudge = tf.math.multiply(err,const)

                # update p and q vals
                p[i].assign(p_i + tf.math.multiply(q_j,nudge))
                q[:,j].assign(q_j + tf.math.multiply(p_i,nudge))
            printc(f" in {time()-t1} seconds",TAN)

    return p,q

@tf.function
def GradientDescent_optimized(A,filter_matrix,dim=10,alpha=.1,iters=1):
    # Ascertain what dimensions we are in
    rows    = tf.Variable(A.shape[0],dtype=tf.dtypes.int32)
    cols    = tf.Variable(A.shape[1],dtype=tf.dtypes.int32)
    # Create the P and Q matrices
    p       = tf.Variable(tf.random.uniform(shape = [rows,dim],dtype=tf.dtypes.float32))
    q       = tf.Variable(tf.random.uniform(shape = [dim,cols],dtype=tf.dtypes.float32))

    # init the constants for a loop
    iteration = tf.Variable(0,dtype=tf.dtypes.int32)

    # Run 'iter' times
    while tf.less(iteration,iters):
        i = tf.Variable(0,dtype=tf.dtypes.int32)
        j = tf.Variable(0,dtype=tf.dtypes.int32)
        iteration.assign_add(1)
        # iter through cols
        while tf.less(j, cols):

            # iter through rows
            while tf.less(i, rows):

                # skip if 0
                if tf.equal(0,filter_matrix[i][j]):
                    i.assign_add(1)
                    continue

                # get q col and p row
                q_j = q[:,j]
                p_i = p[i]

                # find the err present
                err = tf.math.subtract(A[i][j],tf.tensordot(q_j,p_i,axes=1))

                # find where to nudge down the gradient
                nudge = tf.math.multiply(err,alpha)

                # update p and q vals
                p[i].assign  (tf.math.add(  p_i,    tf.math.multiply(q_j,nudge)))
                q[:,j].assign(tf.math.add(  q_j,    tf.math.multiply(p_i,nudge)))

                i.assign_add(1)
            j.assign_add(1)


    return p,q

@tf.function
def update_val(err,alpha,q,j):

    return tf.math.multiply(    tf.transpose(tf.gather(q,[j],axis=1)),  tf.math.multiply(alpha,err))

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
