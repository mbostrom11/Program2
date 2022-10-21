from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future
from multiprocessing import Pool
import MA4_1

def f(x):
    return x*x

if __name__ == "__main__":
    start = pc()
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")


def runner(n):
    print(f"Performing costly function {n}")
    pause(n)
    return f"Function {n} has completed"

if __name__ == "__main__":
    
    start = pc()

    with future.ProcessPoolExecutor() as ex:
        p = [5, 4, 3, 2, 1]
        results = ex.map(runner, p)

        for r in results:
            print(r)
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")



###

def generator(n):
    list1=[]
    while n>0:
        list1.append(random.uniform(-1,1))
        n = n-1
    return list1 

def in_out(x,y):
    color =[]
    for i in range(len(x)):
         if (x[i])**2 + (y[i])**2 <= 1:
            color.append('r')
         else:
            color.append('b')
    return color
x1 = generator(1000)
y1 = generator(1000)
color1 = in_out(x1,y1)
aprox1 = (4*color1.count('r'))/1000

x2 = generator(10000)
y2 = generator(10000)
color2 = in_out(x2,y2)
aprox2 = (4*color2.count('r'))/10000

x3 = generator(100000)
y3 = generator(100000)
color3 = in_out(x3,y3)
aprox3 = (4*color3.count('r'))/100000

print(math.pi)
print(aprox1)
print(aprox2)
print(aprox3)

plt.scatter(x1,y1,c=color1)
plt.show()

plt.scatter(x1,y1,c=color1)
plt.show()

plt.scatter(x2,y2,c=color3)
plt.show()



print(hypersphere(100000,2))
print(actual(2))
print(hypersphere(100000,11))
print(actual(11))