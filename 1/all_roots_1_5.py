#!/usr/bin/env python

"""
Determine all roots of a given function using a combined
Bisection/Newton-Rhapson Iteration that has been provided. 

Solution to Problem Set 1, Problem 5.
Avichal Kaul

To run:
	./all_roots_1_5.py


We add the code from both Newton's Method and the Bisection
Algorithm and use the general outline provided in the notes:
Choose starting values for each root manually, take the
midpoint to start the Newton iteration, if it is within
bounds we keep using it, if not we use bisection, and repeat
for each of the roots.
"""

import numpy as np

mid = lambda low, high: (low + high) / 2 ## global funcs
f = lambda x: x**3 - 25*x**2 + 165*x - 275 ## target function

def main():
	root_bounds = [[2, 3], [6, 7], [15, 16]] ## manually selected bounds for each root
	error = 0.001
	j = 0
	for i in root_bounds:
		med = mid(i[0], i[1])
		while np.abs(f(med)) > error: ## checking that the result is within tolerance
			med = meme(i, med)
		j += 1
		print(f'Root {j}: {med}. f(root): {f(med)}')

def meme(root_bound, med):
	## Combined Bisection/Newton-Rhapson's Method
	x, dx = get_vals(med)
	if newtons_method(med, x, dx) > root_bound[0] and newtons_method(med, x, dx) < root_bound[1]:
		return newtons_method(med, x, dx)
	return bisection(med, root_bound)

def bisection(med, root_bound): ## same bisection function as before
	low = root_bound[0]
	high = root_bound[1]
	if f(low)*f(high) < 0: ## checking that the root is actually bound
		med = mid(low, high)
		if f(low)*f(med) < 0:
			high = med
		else:
			low = med
	return mid(low, high) ## returns the midpoint for Newton's method to use

def newtons_method(x, f, df):
	return x - f / df

def get_vals(x):
	df = lambda x: 3*x**2 - 50*x + 165 ## derivative
	return f(x), df(x)

if __name__ == "__main__":
	main()
