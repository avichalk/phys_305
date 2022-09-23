#!/usr/bin/env python

"""
Perform bisection on the root nearest x=0 of tanx-3. Plot
the results and the process, compare to the analytical solution.

Solution to Problem Set 1, Problem 3.
Avichal Kaul

To run:
	./bisection_1_3.py


Using an algorithm where we use upper bounds, lower bounds,
and a midway. If f(up) and f(low) have opposite signs, we
continue with the process. We calculate the midway, and see
if that has an opposite sign to the lower bound. If yes, the
midway becomes the new upper bound. If no, the midway becomes
the new lower bound. We keep going until an acceptable error,
at which point we terminate the program.
"""

import matplotlib.pyplot as plt
import numpy as np
import sys

def main():
	low = 0 ## set low and high bounds based on
	high = 1.5 ## guesstimate and periodicity of tanx
	error = 1e-6 ## interestingly, setting it to 0 means eventually floating point rounding errors
	x = np.arange(low,high,0.1) ## give you an answer
	y = np.tan(x) - 3 ## this will shift tanx down by 3 units

	plt.plot(x, y)
	# plt.show()

	mid = lambda low, high: (low + high) / 2
	mtan = lambda x: np.tan(x) - 3
	med = high ## midway, needed this here to start the loop

	i = 0
	while np.abs(mtan(med)) > error: ## we run until the error is acceptable
		if mtan(low)*mtan(high) < 0:
			med = mid(low, high) 
			if mtan(low)*mtan(med) < 0:
				high = med
			else:
				low = med
		#print(low, high, med)
		plt.axvline(x=low, color='red', linestyle='--') ## fancy dotted lines
		plt.axvline(x=high, color='blue', linestyle='--')
		plt.pause(0.5) ## updates the graph live
		i += 1
		
		sys.stdout.write("\rIteration Number %i" % i) ## fancy print
		sys.stdout.flush()

	print()
	print(f'Root is {mid(low, high)}')
	print(f'tan({mid(low, high)}) - 3 = {mtan(mid(low, high))}')
	#print(f'Error: {np.abs(mtan(mid(low, high))-np.arctan(3))}')

	plt.show()

if __name__ == "__main__":
	main()
