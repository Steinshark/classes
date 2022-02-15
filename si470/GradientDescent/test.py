import pandas as pd
from os.path import join
import numpy as np
import os
import sys
from time import time
import pprint
from sklearn.decomposition import TruncatedSVD
import scipy



def load_data():
    self.datasets = {
                    'small'     :  {'movies'        : join('ml-latest-small','movies.csv') , 'ratings' : join("ml-latest-small","ratings.csv") , 'tags' : join("ml-latest-small","tags.csv")},
                    'large'     :  {'movies'        : join("ml-latest","movies.csv")       , 'ratings' : load_from[self.input_source]       , 'tags' : join('ml-latest',"tags.csv")},
                    'usna'      :  {'foodMovies'    : 'foodAndMovies.csv'}}                                #join("ml-latest","ratings.csv")

    self.dataframes= {
                    'small'     :  {'movies'        : None, 'ratings' :  None, 'tags' : None},
                    'large'     :  {'movies'        : None, 'ratings' :  None, 'tags' : None}}


    self.headers = ["Black Panther","Pitch Perfect","Star Wars: The Last Jedi","It","The Big Sick","Lady Bird","Pirates of the Caribbean","Despicable Me","Coco","John Wick","Mamma Mia","Crazy Rich Asians","Three Billboards Outside Ebbings, Missouri","The Incredibles"]

def read_data(self):

    # Read in all CSVs to DataFrames
    printc(f"\nBEGIN: Data read from CSV",BLUE,endl='')
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
    printc(f"\tsize: {(self.ratings.memory_usage().sum() / (1024.0*1024.0)):.2f} MB",TAN)

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
    self.n_movies                            = int( len(    self.dataframes['large']['movies']     ['movieId']                     ))
    self.n_users                             = int(         self.ratings                           ['userId'].iloc     [-1]        )

    # Fix the mapping of movieId to col in matrix
    self.movieId_to_col = {}
    self.movieId_to_name = {}
    self.col_to_movieId = {}
    i = 0
    with open(self.datasets['large']['movies'],'r',encoding='utf-8') as file:
        file.readline()
        for line in file:
            movieID = int(line.split(',')[0])
            movieName = line.split(',')[1]
            self.movieId_to_col[movieID] = i
            self.movieId_to_name[movieID] = movieName
            self.col_to_movieId[i] = movieID
            i += 1

    self.liked_movies = list(map(lambda x : self.movieId_to_col[x], self.liked_movies))

    # Done with data read!
    printc(f"Read Data in {(time()-t1):.3f} seconds",GREEN)
    printc(f"Expecting to build matrix size ({self.n_movies},{self.n_users})",TAN)
