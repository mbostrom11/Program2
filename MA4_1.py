#1
import random
import math
from matplotlib import pyplot as plt



#2
#def Extract(data,n):
#	return list(list(zip(*data))[n])

#2^d *all points in sphere /n

def square(list):
    return map(lambda x: x ** 2, list)

def hypersphere(n,d):
    final=0
    count =0
    while count < n:
        list2=[]
        list2 = [random.uniform(-1,1) for x in range(0,d)]
        if (sum(list(square((list2))))) <= 1:
            final = final+1
        count = count + 1
    return 2**d * final/n
        
#    return ((2**d)*(len(incirc)/n ))

def actual(d):
    return (math.pi**(d/2))/(math.gamma(d/2+1))







if __name__ == "__main__":
    from time import perf_counter as pc
    from time import sleep as pause
    import concurrent.futures as future
    tstart2 = pc()
    with future.ProcessPoolExecutor() as ex:
        z = ex.map(hypersphere,[100000]*10,[11]*10)
    tstop2 = pc()
    print(f"Measured time: {tstop2 -tstart2} seconds")