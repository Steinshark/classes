import pandas as pd
from os.path import join
import numpy as np

import scipy
import os
import sys
from time import time
import pprint
from sklearn.decomposition import SparsePCA, IncrementalPCA, TruncatedSVD
from sklearn.neighbors import KNeighborsClassifier

from matplotlib import pyplot as plt

times = {'start' : time()}
# Package import to work on windows and linux
sys.path.append("C:\classes")
sys.path.append("D:\classes")
sys.path.append("/home/mids/m226252/classes/")

from Toolchain.terminal import *

import signal

def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)

signal.signal(signal.SIGINT, handler)

class ExecuteJob:
    def __init__(self, liked_movies,model_replacement='mean'):
        # Give us some nice things to know and set some settings
        self.replace = model_replacement
        # This will be used to find predictions
        self.liked_movies = [122906,96588,179819,175303,168326,177615,6539,79091,161644,115149,60397,192283,177593,8961]

    ################################################################################
    #                           Manage Logging
    ################################################################################
    def prepare_data(self):
        self.datasets = {    'small'     :  {'movies'        : join('ml-latest-small','movies.csv') , 'ratings' : join("ml-latest-small","ratings.csv") , 'tags' : join("ml-latest-small","tags.csv")},
                        'large'     :  {'movies'        : join("ml-latest","movies.csv")       , 'ratings' : join("ml-latest","ratings.csv")       , 'tags' : join('ml-latest',"tags.csv")},
                        'usna'      :  {'foodMovies'   : 'foodAndMovies.csv'}}

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
                    printc(f"\treading {dset}-{size}",TAN,endl='')
                    self.dataframes[size][dset]   = pd.read_csv(self.datasets[size][dset],sep=',')
                    printc(f"\n\tsize: {(self.dataframes[size][dset].memory_usage().sum() / (1024.0*1024.0)):.2f} MB\n",TAN,endl='')

        # Read larger 'ratings' dataset
        printc(f"\treading ratings-large",TAN)
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
        self.n_movies                            = int(         self.dataframes['large']['movies']     ['movieId'].iloc    [-1]        )
        self.n_users                             = int(         self.ratings                           ['userId'].iloc     [-1]        )

        # Done with data read!
        printc(f"Read Data in {(time()-t1):.3f} seconds",GREEN)

    def show_data(self):
        printc(f"\n\nDATASET: ",BLUE)

        printc(f"{TAN}'ratings' looks like:  {END}\n"   +   \
                    f"{self.ratings.head(3)}                               \n\n",TAN)

        printc(f"{TAN}'movies' looks like:   {END}\n"   +   \
                    f"{self.dataframes['large']['movies'].head(3)}    \n\n",TAN)

        printc(f"{TAN}number of users:       {END}  "   +   \
                    f"{self.n_users}                                  ",TAN)

        printc(f"{TAN}number of movies:      {END}  "   +   \
                    f"{self.n_movies}                                 \n\n",TAN)

    def run_svd(self,n,alg):
        t1 = time()

        tsvd = TruncatedSVD(n_components=n, algorithm=alg,n_iter=3)
        m_reduced = tsvd.fit_transform(self.matrix)
        t2 = time()-t1
        printc(f"{n} took {(t2):.3f}s to calculate with {RED}{alg}",GREEN)
        printc(f"\tvar: {tsvd.explained_variance_ratio_.sum(): .4f} in {n} dimensions ",TAN)

        np.save(f"SVD_DECOMP{n}",m_reduced)
        return tsvd.explained_variance_ratio_.sum(), t2



    def create_matrix(self):
        rows = self.ratings['movieId'] - 1
        cols =  self.ratings['userId'] - 1
        self.matrix = scipy.sparse.coo_matrix((self.ratings['rating'],(rows,cols)),shape=[self.n_movies,self.n_users])


    def run(self):
        # Prepare the datasets with defintions for filenames
        self.prepare_data()

        # Load the data into RAM
        self.read_data()

        # Give the user some useful things to know
        self.show_data()

        # Init our tensors for building the matrix later
        self.create_matrix()

        times = {"arpack" : [], "rand" : []}
        varia = {"arpack" : [], "rand" : []}
        try:
            n_it = list(map(lambda x : int(x),sys.argv[1:]))
        except:
            n_it = [1500]

        for n in n_it:
            printc(f"Running n={n}",BLUE)

            v, t = self.run_svd(n,'arpack')
            times['arpack'].append(t/60)
            varia['arpack'].append(v)

            v, t = self.run_svd(n,'randomized')
            times['rand'].append(t/60)
            varia['rand'].append(v)

        plt.plot(n_it,varia['arpack'],"ro",label="variance_ar")
        plt.plot(n_it,times['arpack'],"r--",label="calc time_ar")

        plt.plot(n_it,varia['rand'],"go",label="variance_r")
        plt.plot(n_it,times['rand'],"g--",label="calc time_r")

        plt.xlabel("n value")
        plt.ylabel("time (min) / variance")
        plt.legend()

        plt.show()
if __name__ == "__main__":
    movies = [122906,96588,179819,175303,168326,177615,6539,79091,161644,115149,60397,192283,177593,8961]
    job = ExecuteJob(movies)
    job.run()
