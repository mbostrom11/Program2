import random
import math
def f(x):
    return x*x
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
