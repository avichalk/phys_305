#!/usr/bin/env python

"""
Evaluates a Gaussian Integral.

Solution to Problem Set 3, Problem 2.
Avichal Kaul

To run:
	./gaussian_integral_3_2.py


Takes the romberg_integration function from our
previous question and runs a new function through it.
Also plots some stuff.
"""

import numpy as np
import matplotlib.pyplot as plt
from romberg_integration_3_1 import romberg_integration

fp = lambda inpt: '{:.5E}'.format((inpt))  ## fancy print

def main():
	P = (1e-10, 10)

	func = lambda x: np.exp(-x**2)
	a = 0
	b = 10

	analytical_res = np.pi ** 0.5
	prog_soln = 2 * romberg_integration(func, a, b, *P)
	#print((prog_soln-analytical_soln)/analytical_soln)
	print(f'Programmatical Solution! {fp(prog_soln)}')
	print(f'Analytical Solution! {fp(analytical_res)}')
	print(f'Percentage Error! {fp((prog_soln-analytical_res)/analytical_res*100)}%')
	

	up = 10
	x = np.arange(2, up)
	y = []
	for i in range(2, up):
		y.append(2 * romberg_integration(func, a, i, *P))

	fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
	ax[0].plot(x, np.array(y))
	ax[0].set_title('Solution Over Time')
	ax[0].set_xlabel('Upper Limit of Integral')
	ax[1].set_xlabel('Upper Limit of Integral')
	ax[1].set_title('Percentage Error over Time')	
	ax[0].set_ylabel('Integrand Solution')
	ax[1].set_ylabel('Percentage Error')
	ax[1].plot(x, (np.array([(i-analytical_res)/analytical_res*100 for i in y])))

	plt.show()


if __name__ == "__main__":
	main()
