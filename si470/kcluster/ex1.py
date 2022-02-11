import tensorflow   as tf
import pandas       as pd 


#Define 
filename    = "docword.nytimes.txt"
docs        = 300000
words       = 102660 
df = pd.read_csv(filename,sep=' ',skiprows=3)
df.columns = ['docId','wordId','count']
print(df.loc['docId','wordId'].head)
