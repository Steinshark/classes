import numpy as np 
import pandas as pd 
import os 
import scipy 

# Read the data into a dataframe 
_RATINGS_SMALL  = os.path.join("ml-latest-small","ratings.csv")
_MOVIE_ID_SMALL = os.path.join("ml-latest-small","movies.csv")
small_ratings   = pd.read_csv(  _RATINGS_SMALL,
                                dtype = {   'userId'    :   np.float32,
                                            'movieId'   :   np.float32,
                                            'rating'    :   np.float32,
                                            'timestamp' :   np.float32})

# Convert the dataframe to correct matrix format: (rows=MovieId, cols=userId)
small_ratings_matrix = small_ratings.pivot( index='movieId',    columns='userId',   values='rating')


data_size = len(small_ratings_matrix)


print(f"data is size: {data_size}")