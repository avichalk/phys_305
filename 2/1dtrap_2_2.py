#!/usr/bin/env python

"""
n-th degree Lagrangian interpolation, w/ some extras!

Solution to Problem Set 2, Problem 2.
Avichal Kaul

To run:
	./1dtrap_2_2.py <args> ## REMEMBER TO ADD ARGS!


<how the program works>
"""
import numpy as np
import matplotlib.pyplot as plt

fp = lambda inpt: '{:.5E}'.format((inpt))  ## fancy print

def main():
	a = 0
	b = 1
	ntervals = [50, 100, 200, 400]
	alpha = 2
	func = lambda x: x * np.exp(-alpha * x)
	analytic_int = lambda x: - np.exp(-alpha * x) * (alpha * x + 1) / alpha ** 2

	actual = analytic_int(b) - analytic_int(a) ## actual val of the integral
	
	## Part One
	print('Integral of func b/w provided limits for n = 50: '
	f'{fp(trapezoidalRule(func, a, b, 50))}')
	print()

	rerray, erray = two(func, a, b, ntervals, actual)
	
	## Part Three
	sigmake = lambda x: float('{:g}'.format(float('{:.5g}'.format(x)))) ## code to round to 5 significant figures
	sigtual = sigmake(actual)
	n = 400
	while sigmake(trapezoidalRule(func, a, b, n)) != sigtual:
		n += 200
	print(f'At {n} iterations, {trapezoidalRule(func, a, b, n)}'
	f' matches {actual} to 5 significant figures')
	print()

	## Part Four
	re2ray, e2ray = two(func, a, b, ntervals, actual, four=True)

	#print(erray)	
	#plt.clf()
	fig, ax = plt.subplots()

	plt.plot(np.log(ntervals), np.log(erray), 'r-', label='Part Two Error')
	plt.plot(np.log(ntervals), np.log(e2ray), 'b-', label='Part Four Error')
	plt.legend()
	# plt.plot(np.log(ntervals, np.log(
	plt.xlabel('log (n)')
	plt.ylabel('log (error)')
	plt.show() ## unfortunately, does not look like 1/n^2. REVISE!!
	print()





def two(func, a, b, ntervals, actual, four=False):
	## Part Two (and also part 4?)
	rerray = []
	erray = []

	if not four:
		print('Part Two')
	else:
		print('Part Four')

	for n in ntervals:
		res = trapezoidalRule(func, a, b, n, four)
		error = np.abs((res - actual)/actual)
		erray.append(error)
		rerray.append(res)
		print(f'Error in result for n = {n}: {fp(error)}')

	return rerray, erray

def trapezoidalRule(func, a, b, n, four=False):
	h = (b - a) / n
	ipart1 = func(a) + func(b)
	ipart2 = 0
	i = 1
	denouement = n
	if four: ## changes bounds if we are in part 4
		i -= 1
		denouement += 1
	while i < denouement:
		x = a + i * h
		ipart2 += func(x)
		i += 1
	integral = h / 2 * (ipart1 + 2 * ipart2)
	return integral

if __name__ == "__main__":
	main()
