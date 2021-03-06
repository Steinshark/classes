import tensorflow   as tf
import pandas       as pd 
import numpy        as np

#Define 
filename    = "docword.nytimes.txt"
docs        = 300000
words       = 102660 
df = pd.read_csv(filename,sep=' ',skiprows=3,names=['docId','wordId','count'])
indices = df[['docId','wordId']].apply(np.array,axis=1)

sparse_matrix = tf.sparse.SparseTensor(indices,df['count'],[docs,words])
print(sparse_matrix)
