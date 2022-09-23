#!/usr/bin/env python

"""
Computes the integral of a function between given limits using Romberg Integration, and uses it to solve for the flux leaving a blackbody.

Solution to Problem Set 3, Problem 1.
Avichal Kaul

To run:
	./romberg_integration_3_1.py


The code does its job. I got hung up in a lot of places
because of strange bugs and an incorrect approach (originally
I didn't have an array, instead a series of increasingly complicated
+= statements a la what is there in the trapezoidal function. It might
have worked, but I was also struggling with another bug in the trapezoidal
function where, instead of multiplying by h, I divided by it. Fun.
"""


fp = lambda inpt: '{:.5E}'.format((inpt))  ## fancy print
fprint = lambda inpt: print('{:.5E}'.format((inpt)))  ## do the fancy print

import math
import numpy as np
from astropy import constants as const

def main():
	P = (1e-10, 10) ## erg, n_max

	a = 0
	b = 100
	analytical_res = np.pi ** 4 / 15

	func = lambda x: 0 if x == 0 else x**3 / (np.exp(x) - 1) #nd# you need to deal with the singularity before integrating?
	i = romberg_integration(func, a, b, *P) ## code it in as a special case? idfk 
	#print(i)
	#print(analytical_res)

	soln = lambda res: 2*np.pi/const.c.cgs**2*(const.k_B.cgs**4)/const.h.cgs**3*res ## bless you astropy
	print(f'Programmatical Solution! {fp(soln(i))}')
	print(f'Analytical Solution! {fp(soln(analytical_res))}')
	print(f'Percentage Error! {fp((soln(i)-soln(analytical_res))/soln(analytical_res)*100)}%')

def next_trapezoidal(func, a, b, n):
	N = 2 ** n
	h = (b - a) / N
	In = 0
	#print(N/2+1)
	for j in range(1, int(N / 2 + 1)):
		In += func(a + (2*j - 1)*h) ## i spent three hours debugging because instead of multiplying by h i divided by h
		#print(func(a + (2 * j - 1) / h)) ## the way the font slopes in the pseudocode made me think it was /h. 
	return h * In


def romberg_integration(func, a, b, eps, n_max):
	i = np.array([[0] * (n_max + 1)] * (n_max + 1), float) ## is there a python array bug i am forgetting about?
	i[0][0] = 0.5 * (b - a) * (func(a) + func(b)) ## yes, there was a python array bug i was forgetting about.
	#print(i[0][0])
	
	for n in range(1, n_max + 1):
		# i_prev = i ## i_n-1, 0
		i[n][0] = 0.5 * i[n-1][0] + next_trapezoidal(func, a, b, n) ## i_n, 0
		#print(next_trapezoidal(func, a, b, n)) ## i_n, 0

		#print(i[n][0])
		#ink_prev = i_prev ## i_n-1, 0

		for k in range(1, n + 1): ## we need i_n, 0 and i_n-1, 0
			q = 4**k ## how do we get k-1? another for loop?
			i[n][k] = (q * i[n][k-1] - i[n-1][k-1]) / (q - 1) ## i_n, k = i_n, k-1: i_n-1, k-1
			#print(i[n][k])
			# i_prev = i ## i_n, k-1
	
		if np.abs(i[n][n] - i[n][n-1]) < eps * np.abs(i[n][n-1]):
			return i[n][n]
	#print(i)
	print('Failed to converge!')


if __name__ == "__main__":
	main()
