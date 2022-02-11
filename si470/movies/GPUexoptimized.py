import tensorflow as tf
import pandas as pd
from os.path import join
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import sys
from time import time
import pprint

times = {'start' : time()}
# Package import to work on windows and linux
sys.path.append("C:\classes\")
sys.path.append("D:\classes")
sys.path.append("/mnt/d/classes")
sys.stderr = sys.stdout
print(sys.path)
from Toolchain.terminal import *
from Toolchain.GPUTools import *



class ExecuteJob:
    def __init__(self, liked_movies,model_replacement='mean'):
        # Give us some nice things to know and set some settings
        printc(f"Num GPUs Available: {len(tf.config.list_physical_devices('GPU'))}\n\n",GREEN)
        self.replace = model_replacement
        # This will be used to find predictions
        self.liked_movies = [122906,96588,179819,175303,168326,177615,6539,79091,161644,115149,60397,192283,177593,8961]

        # Type definitions
        self.f_64 = tf.dtypes.float64
        self.i_32 = tf.dtypes.int32
        self.i_64 = tf.dtypes.int64
    ################################################################################
    #                           Manage Logging
    ################################################################################
    def prepare_data(self):
        self.datasets = {    'small'     :  {'movies'        : join('ml-latest-small','movies.csv') , 'ratings' : join("ml-latest-small","ratings.csv") , 'tags' : join("ml-latest-small","tags.csv")},
                        'large'     :  {'movies'        : join("ml-latest","movies.csv")       , 'ratings' : join("ml-latest","ratings.csv")       , 'tags' : join('ml-latest',"tags.csv")},
                        'usna'      :  {'foodMovies'   : 'foodAndMovies.csv'}}                                #join("ml-latest","ratings.csv")

        self.dataframes= {   'small'     :  {'movies'        : None, 'ratings' :  None, 'tags' : None},
                        'large'     :  {'movies'        : None, 'ratings' :  None, 'tags' : None}}


        self.headers = ["Black Panther","Pitch Perfect","Star Wars: The Last Jedi","It","The Big Sick","Lady Bird","Pirates of the Caribbean","Despicable Me","Coco","John Wick","Mamma Mia","Crazy Rich Asians","Three Billboards Outside Ebbings, Missouri","The Incredibles"]

    def read_data(self):

        # Read in all CSVs to DataFrames
        printc(f"BEGIN: Data read from CSV",BLUE)
        t1 = time()
        for size in self.datasets:
            for dset in self.datasets[size]:
                if not (size == 'large' and dset == 'ratings') and not (size == 'usna' and dset == 'foodMovies'):
                    # Read and print status
                    printc(f"\n\treading {dset}-{size}",TAN,endl='')
                    self.dataframes[size][dset]   = pd.read_csv(self.datasets[size][dset],sep=',')
                    printc(f"\n\tsize: {(self.dataframes[size][dset].memory_usage().sum() / (1024.0*1024.0)):.2f} MB",TAN,endl='')

        # Read larger 'ratings' dataset
        printc(f"\n\treading ratings-large",TAN)
        self.ratings        = pd.read_csv(  self.datasets['large']['ratings'],
                                            dtype   =   {   'userId'    :   np.float32,
                                                            'movieId'   :   np.float32,
                                                            'rating'    :   np.float64,
                                                            'timestamp' :   np.float64},
                                            sep     =   ',')
        printc(f"\tsize: {(self.ratings.memory_usage().sum() / (1024.0*1024.0)):.2f} MB\n\n",TAN)

        # Gather the USNA data and prepare it
        self.usna           = pd.read_csv(  self.datasets['usna']['foodMovies'],     sep = ',')[self.headers]

        # Fix USNA data with MEAN
        for col in self.headers:
            if self.replace     == 'mean':
                replacement = self.usna[col].mean()
            elif self.replace   == 'zero':
                replacement = 0
            self.usna[col].fillna(value = 0, inplace = True)

        # Some helpful constants                                  dataset                             column                index
        self.n_movies                            = int(         self.dataframes['large']['movies']     ['movieId'].iloc    [-1]        )
        self.n_users                             = int(         self.ratings                           ['userId'].iloc     [-1]        )

        # Done with data read!
        printc(f"\tRead Data in {(time()-t1):.3f} seconds",GREEN)

    def show_data(self):
        printc(f"\n\nDATASET: ",BLUE)

        printc(f"{BLUE}'ratings' looks like:  {END}\n"   +   \
                    f"{self.ratings.head(3)}                               \n\n",TAN)

        printc(f"{BLUE}'movies' looks like:   {END}\n"   +   \
                    f"{self.dataframes['large']['movies'].head(3)}    \n\n",TAN)

        printc(f"{BLUE}number of users:       {END}  "   +   \
                    f"{self.n_users}                                  ",TAN)

        printc(f"{BLUE}number of movies:      {END}  "   +   \
                    f"{self.n_movies}                                 \n\n",TAN)

    def create_init_tensors(self):
        printc(f"Building Index and Value Tensors\n\n",GREEN)
        t1 = time()

        # Set x,y index arrays and build index tensor (n_movies,x)
        matrix_x        = tf.convert_to_tensor(self.ratings['userId'].apply(lambda x : x - 1),  dtype=self.i_64)
        matrix_y        = tf.convert_to_tensor(self.ratings['movieId'].apply(lambda x : x - 1), dtype=self.i_64)
        self.indices    = tf.stack( [matrix_y,matrix_x],    axis = 1)
        # Build value tensor
        self.values     = tf.convert_to_tensor(self.ratings['rating'],  dtype=self.f_64)
        self.values    =  tf.transpose(self.values)
        # Info
        printc(f"\tFinished Tensor build in\t{(time()-t1):.3f} seconds",GREEN)
        printc(f"\tindices:\t{self.indices.shape}\n\tvalues  : {self.values.shape}",GREEN)

    def create_sparse_matrix(self):
        self.matrix      = tf.sparse.reorder(tf.sparse.SparseTensor(indices=self.indices,values=self.values,dense_shape = [self.n_movies,self.n_users]))

        s,u,v = tf.linalg.svd(self.matrix)
        input(u)
        printc(f"SHAPE OF MATR: {self.matrix.shape}",GREEN)
        #self.matrix = tf.sparse.transpose(matrix)

    def belongs_in_list(self,dist):
        return (dist < self.closest_movies[self.checkId]['distance']) and not (self.currentId == self.checkId)

    def place_in_list(self,dist):
        self.closest_movies[self.checkId]['distance'] = dist
        self.closest_movies[self.checkId]['movie']    = self.currentId

    def helper_func(self,row_slice):
        row_slice = tf.sparse.reorder(row_slice)
        # Convert to dense matrix and find distance to movie we are predicting for
        dense_row = tf.sparse.to_dense(row_slice)
        distance = euclidean_distance(dense_row, self.current_movie).eval()
        # Update the current movies list
        if self.belongs_in_list(distance):
            self.place_in_list(distance)
        self.currentId =  (1 + self.currentId) % self.n_movies
        if self.currentId % 10000 == 0:
            printc(f"took {(time()-self.t1):.3f} to calc 10000",GREEN)
            self.t1 = time()
        if self.currentId == 0:
            input("made it through a row!",GREEN)
        return distance

    @tf.function
    def run(self):
        # Prepare the datasets with defintions for filenames
        self.prepare_data()

        # Load the data into RAM
        self.read_data()

        # Give the user some useful things to know
        self.show_data()

        # Init our tensors for building the matrix later
        self.create_init_tensors()
        # Build our full sparse matrix (n_movies,n_users)
        self.create_sparse_matrix()

        self.closest_movies = {  movieId     :   {'movie' : 0, 'distance' : 10000.0} for movieId in self.liked_movies }



        ################################################################################
        #                           get slices
        ###############################################################################
        with sess.as_default():
            t1 = time()
            for id in self.liked_movies:

                # The movie we know we like
                self.checkId = id
                self.current_movie = slice_row_sparse(self.matrix,id)
                self.currentId = 0
                # update the current movie recommendations
                self.t1=time()
                distances = tf.map_fn(  self.helper_func,
                                        self.matrix,
                                        dtype=tf.dtypes.float64)

            with open("output",'w') as file:
                file.write(pprint.pformat(self.closest_movies))
            printc(f"FINISHED IN {time()-t1} seconds",GREEN)

if __name__ == "__main__":
    movies = [122906,96588,179819,175303,168326,177615,6539,79091,161644,115149,60397,192283,177593,8961]
    job = ExecuteJob(movies)
    job.run()
