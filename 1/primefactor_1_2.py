#!/usr/bin/env python

"""
Finds prime factors for a number and their multiplicity.

Solution to Problem Set 1, Problem 2.
Avichal Kaul

To run:
	./primefactor_1_2.py <number> <'bar'> ## enable bar to see how long it will take
										  ## (requires installing progressbar)


There is a module called primefac which can do this easily. But I'm assuming
that's not a valid solution.

Brute force approach. In my defense, it works on 10 digit numbers just fine.
And it works on bigger numbers too, just give it like 25 days.
"""

import sys


if len(sys.argv) > 2:
	if sys.argv[2] == 'bar':
		import progressbar ## big numbers take a while
		widgets = [' [', ## to track how much time a big number will take
				 progressbar.Timer(format= 'elapsed time: %(elapsed)s'),
				 '] ',
				   progressbar.Bar('*'),' (',
				   progressbar.ETA(), ') ',
				  ]

def main():
	x = int(sys.argv[1])
	divs = multiples(x) ## finds all multiples of x via brute force.
	primes = {} ## not great, but it works.
	#print(divs)
	for i in divs:
		if len(multiples(i))==0: ## if a factor is prime...
			primes[i] = 1
			#print(multiples(i))
	for i in primes: ## finds multiplicity
		while x % i == 0:
			primes[i] += 1
			x = x / i
	string = ''
	for i in primes:
		string += f'{i}{{{primes[i]}}}  ' ## formatting
	print(string)

def multiples(x):
	divs = []
	i = 2 ## can't use 0 or 1
	try:
		with progressbar.ProgressBar(max_value=x) as bar:
			while i < x:
				if x % i == 0:
					if i not in divs:
						divs.append(i)
				bar.update(i)
				i += 1
	except:
		while i < x:
			if x % i == 0:
				if i not in divs:
					divs.append(i)
			i += 1
	return divs

if __name__ == "__main__":
	main()
