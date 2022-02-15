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
    #      P                      Q
    #[  .  .  .  ]      [  .  .  .  .  .  ]
    #[  .  .  .  ]      [  .  .  .  .  .  ]
    #[  .  .  .  ]      [  .  .  .  .  .  ]
    #[  .  .  .  ]
    #[  .  .  .  ]


# A is assumed to be the unknown values
def RMSE(A,T):

#       sqrt( (1 / T)*(sum(A_ij - (p_i)(q_j))^2) )


    Tinv = tf.reciprocal(tf.norm(T))
    A_sum_err =
    return tf.sqrt(tf.matmul())
