# File location: D:\classes\si470\kcluster\executeGPU.py

from Toolchain.DataTools import *
import sys
from matplotlib import pyplot as plt

_GPU_MODE = False

if __name__ == "__main__":
    if sys.argv[1] == 'GPU':
        import cupy
        _GPU_MODE = True

    matr, docs = load_data(saving_npz=True,read_npz=False,dataset_file='newData',gpuMode=_GPU_MODE)

    n_comp = [1,2,3,4,5,6,7,8,9,10]
    n_time = []

    for n in n_comp:
        newMatr,t = svd_decomp(n=n,matrix=matr)
        printc(f"{rmse(matr,newMatr)}",TAN)
        n_time.append(t/60)
    plt.scatter(n_comp,n_time)
    plt.show()
