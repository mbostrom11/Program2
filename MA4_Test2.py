from multiprocessing import Pool
import defs

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(defs.hypersphere, [100000]*10,[11]*10))


import time
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future
list1 = []
tstart2 = pc()
with future.ProcessPoolExecutor() as ex:
    z = ex.map(defs.hypersphere,[100000]*10,[11]*10)
    dat = list1.append(z)
tstop2 = pc()
print(f"Measured time: {tstop2 -tstart2} seconds")