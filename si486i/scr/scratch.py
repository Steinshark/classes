from hashlib import sha3_256
from random import randint
from string import ascii_lowercase, ascii_uppercase
from time import time
from matplotlib import pyplot as plt

def make_string(l=20):
    al = f"{ascii_lowercase}{ascii_uppercase}{''.join(['0','1','2','3','4','5','6','7','8','9','0'])}"
    return ''.join([al[randint(0,len(al)-1)] for _ in range(l)])

def make_zeros(leading=5):
    l = ''.join(['0' for i in range(leading)])
    s = make_string(l=20)
    h = sha3_256()
    h.update(s.encode())
    h = h.hexdigest()
    while not h[:leading] == l:
        s = make_string(l=20)
        h = sha3_256()
        h.update(s.encode())
        h = h.hexdigest()
    return h

if __name__ == "__main__":

    x_sets = [[],[],[]]
    y_sets = [[],[],[]]
    for leads in range(1,6):
        for repeat in range(3):
            t1 = time()
            hash = make_zeros(leading=leads)
            ttaken = time()-t1
            x_sets[repeat].append(leads)
            y_sets[repeat].append(ttaken)
            print(f"{hash} found in {ttaken} seconds")
    for i,x in enumerate(x_sets):
        plt.scatter(x,y_sets[i])
    plt.show()
