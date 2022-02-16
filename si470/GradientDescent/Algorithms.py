import tensorflow as tf
import numpy as np
def GradientDescent(real_data,alpha=.1,iters=1000):

    # Ascertain what dimensions we are in
    cols    = real_data.shape[0]
    rows    = real_data.shape[1]

    # Create the P and Q matrices
    dim = 3
    p_init   = tf.random.uniform(shape = [cols,dim],dtype=tf.dtypes.float32)
    q_init   = tf.random.uniform(shape = [dim,rows],dtype=tf.dtypes.float32)
    print(p_init)
    print(q_init)
    return p_init,q_init

# A is assumed to be the unknown values
def RMSE(A,T,p,q):
#       sqrt( (1 / T)*(sum(A_ij - (p_i)(q_j))^2) )
    # 1 / T
    printc(f"T is shape {A.shape}")
    Tinv = tf.reciprocal(tf.constant([A.shape[0])],dtype=tf.dtypes.float32))
    # p,q
    pq = tf.matmul(p,q)
    A_pq = tf.math.subtract(A,pq)
    A_pq_square = tf.square(A_pq)
    sum = tf.reduce_sum(A_pq_square)
    return tf.sqrt(sum)


if __name__ == "__main__":
    a = tf.constant([[1,2,3],[4,5,6]],dtype=tf.dtypes.float32)
