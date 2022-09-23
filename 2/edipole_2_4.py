#!/usr/bin/env python

"""
'Use the Trapezoidal Rule to perform a double integral to find charge'

Solution to Problem Set 2, Problem 4.
Avichal Kaul

To run:
	./edipole_2_4.py <args> ## REMEMBER TO ADD ARGS!


As we can see, the error does not converge. It stays at 1.
"""
import numpy as np
import matplotlib.pyplot as plt

def main():
	ns = [50, 100, 200, 400]
	q = 1.68e-19
	correct = q/(4*np.pi)*8*np.pi ## analytical solution
	P = (0, 2*np.pi, 0, np.pi)
	nums = []
	errors = []
	for i in range(len(ns)):
		res = comptrap2D(ns[i], ns[i], *P)
		nums.append(res)
		errors.append(np.abs((res-correct)/correct))

	#print(nums)
	#print(errors)

	plt.plot(ns, errors)
	plt.show()


def fx(theta, phi):
	dR = 0.1
	f = (2 + dR * np.cos(phi) * np.sin(theta)) * np.sin(theta)
	return f

def comptrap2D(n, m, a, b, c, d):
	hx = (b - a) / n
	hy = (d - c) / m
	integral = 0
	q = 1.68e-19
	for i in range(n):
		for j in range(n):
			xi = hx / 2 + i * hx + a
			yj = hy / 2 + j * hy + c
			integral += hx * hy * fx(xi, yj)

	return q/(4*np.pi)*integral


if __name__ == "__main__":
	main()
