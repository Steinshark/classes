################################################################################
#                           IMPORTS
################################################################################
from tensorflow import square, reduce_sum, sqrt


# Computes the euclidean distance of tensors A and B 
def GPU_euclidean_dista(A,B):

    # Error Check
    if not A.shape == B.shape:
        printc(f"\tshape mismatch A: {A.shape}, B: {B.shape}")

    #ALGORITHM

    # 1 - Calc pointwise difference
    subMatrix = A - B

    # 2 - Find square of distance
    squareMatrix = tf.square(subMatrix)

    # 3 = Find the sum of the square distance
    sumMatrix = tf.reduce_sum(squareMatrix)

    # 4 - return the squareroot of the sumMatrix
    return tf.sqrt(sumMatrix)
