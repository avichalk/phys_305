#!/usr/bin/env python

"""
Use Newton's Method to find a minimum value of a function.

Solution to Problem Set 1, Problem 4.
Avichal Kaul

To run:
	./newtons_min_1_4.py


The minimum is the root of the first derivative of the function.
So, we use Newton's Method on the first derivative of the function.

The analytical solution is 1.205, so with rounding our answer matches.
"""

import numpy as np

def main():
	x_0 = 1 ## initial approximation
	error = 1e-6
	i = 0
	x_1 = newtons_method(x_0)
	while np.abs(x_1 - x_0) > error:
		x_0 = x_1
		x_1 = newtons_method(x_0)
		i += 1
		print(f'Iteration {i}: {x_1}')

def newtons_method(x):
	f = lambda x: 4*x**3 - 7 ## derivative of target
	df = lambda x: 12*x**2 ## second derivative
	return x - f(x)/df(x)


if __name__ == "__main__":
	main()
