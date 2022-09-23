#!/usr/bin/env python

"""
Computes the integral of a function between given limits using Romberg Integration, and uses it to solve for the flux leaving a blackbody.

Solution to Problem Set 3, Problem 1.
Avichal Kaul

To run:
	./romberg_integration_3_1.py <args> ## REMEMBER TO ADD ARGS!


<how the program works>
"""


fp = lambda inpt: '{:.5E}'.format((inpt))  ## fancy print
fprint = lambda inpt: print('{:.5E}'.format((inpt)))  ## do the fancy print

import math
import numpy as np

def main():
	eps = 1e-6

	a = 0
	b = 100
	analytical_res = np.pi ** 4 / 15


	func = lambda x: 0 if x == 0 else x**3 / (math.exp(x) - 1) ## you need to deal with the singularity before integrating?
	i = romberg_integration(func, a, b, eps) ## code it in as a special case? idfk 
	print(i)

def next_trapezoidal(func, a, b, n):
	N = 2 ** n
	h = (b - a) / N
	In = 0
	for j in range(1, int(N / 2 + 1)):
		In += func(a + (2 * j - 1) / h)
			
	return h * In


def romberg_integration(func, a, b, eps,):
	n_max = 7
	i = 0.5 * (b - a) * (func(b) + func(a))
	
	for n in range(1, n_max):
		i_prev = i ## i_n-1, 0
		i = 0.5 * i + next_trapezoidal(func, a, b, n) ## i_n, 0
		#ink_prev = i_prev ## i_n-1, 0

		for k in range(1, n): ## we need i_n, 0 and i_n-1, 0
			q = 4**k ## how do we get k-1? another for loop?
			i = (q * i - i_prev) / (q - 1) ## i_n, k = i_n, k-1: i_n-1, k-1
			i_prev = i ## i_n, k-1


		print(i)	
		if abs(i - i_prev) < eps * abs(i_prev):
			return i

	print('get naenaed lmao')


if __name__ == "__main__":
	main()
