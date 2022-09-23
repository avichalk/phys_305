#!/usr/bin/env python

"""
Using the one-dimensional Trapezoidal Method to
programatically approximate the value of integrals w/ some extras!

Solution to Problem Set 2, Problem 1.
Avichal Kaul

To run:
	./ndegLinterpol_2_1.py <args> ## REMEMBER TO ADD ARGS!


<how the program works>
"""

## UNFINISHED!!

import numpy as np
import sys
import matplotlib.pyplot as plt

def main():	
	a = -3.1415
	b = -a
	ntervals = 	[3, 5, 9, 13, 17]
	fx = lambda inpt: np.sin(inpt)
	x = 0.127
	nterrors = []

	for n in ntervals:
		xi, yi = split_line(a, b, n, fx)
		if len(sys.argv) > 1:
			x = float(sys.argv[1])
		#plt.plot(xi, yi)
		#plt.show()
		
		res = lagrunge(xi, yi, n, x)
		print('Approximate value of %.3f for %i iterations' % (res, n))
		rel_error = np.abs(res - fx(x))/np.abs(fx(x))
		nterrors.append(rel_error)
		print('Relative Error: %.3f.' % rel_error)
	
	plt.plot(ntervals, nterrors)
	plt.show()

def split_line(a, b, n, fx):
	## Figure out the interval distance 
	## and all the points along it.

	xi = []
	yi = []
	for i in range(n + 1):
		xi.append(a + i * (b - a) / n)
		yi.append(fx(i))
	return xi, yi

def lagrunge(xi, yi, n, x):
	## Using an idea I found online
	res = 0.0
	for i in range(n):
		z = 1
		for j in range(n):
			if j != i:
				z = z * (x - xi[j]) / (xi[i] - xi[j])
		res = res + z * yi[i]
	return res

if __name__ == "__main__":
	main()
