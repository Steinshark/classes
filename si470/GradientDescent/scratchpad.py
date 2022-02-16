import tensorflow as tf


s = tf.sparse.from_dense([[1, 2, 0],
                          [0, 4, 0]])

                          
h = tf.sparse.to_dense(tf.sparse.map_values(tf.ones_like, s)).numpy()
print(h)
