#!/usr/bin/env python3
import random
from person import Person
from numba import njit
from time import perf_counter as pc
from matplotlib import pyplot as plt
def fib_py(n):
	if n<= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))
@njit
def fib_numba(n):
	if n<= 1:
		return n
	else:
		return(fib_numba(n-1) + fib_numba(n-2))

def main():
	f = Person(5)
	print(f.get())
	f.set(47)
	print(f.fib())
	print(fib_numba(47))
	n = [*range(30, 45, 1)]
	n1 =[*range(20, 30, 1)]
	sec1 = []
	sec2 = []
	sec3 = []
	sec4 = []
	sec5 = []
	for i in n:
		f = Person(i)
		tstart1 = pc()
		f.fib()
		tstop1 = pc()
		sec1.append((tstop1-tstart1))
		tstart2 = pc()
		fib_numba(i)
		tstop2 = pc()
		sec2.append((tstop2-tstart2))
		tstart3 = pc()
		fib_py(i)
		tstop3 = pc()
		sec3.append((tstop3-tstart3))
	for i in n1:
		tstart4 = pc()
		fib_numba(i)
		tstop4 = pc()
		sec4.append((tstop4-tstart4))
		tstart5 = pc()
		fib_py(i)
		tstop5 = pc()
		sec5.append((tstop5-tstart5))
	plt.scatter(n,sec1,c='r')
	plt.scatter(n,sec2,c='b')
	plt.scatter(n,sec3,c='g')
	plt.savefig('Test1.png',dpi=300)
	plt.clf()
	plt.scatter(n1,sec4,c='r')
	plt.scatter(n1,sec5,c='b')
	plt.savefig('Test2.png',dpi=300)
if __name__ == '__main__':
	main()
