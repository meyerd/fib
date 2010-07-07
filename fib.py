#!/usr/bin/python

import math
import sys

# naive recursion
def fib_rek(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fib_rek(n-1) + fib_rek(n-2)

# dynamic programming
def fib_mem(n):
	m = []
	for i in range(n+1):
		m.append(-1)
	m[0] = 0
	m[1] = 1
	def fib_mem_rek(n):
		if m[n] != -1:
			return m[n]
		else:
			val = fib_mem_rek(n-1) + fib_mem_rek(n-2)
			m[n] = val
			return val
	return fib_mem_rek(n)

# moivre-binet formula
def fib_close(n):
	return int((1.0 / math.sqrt(5)) * (math.pow(((1.0 + math.sqrt(5)) / 2), n) - math.pow(((1.0 - math.sqrt(5)) / 2), n)))

if __name__ == '__main__':
	from timeit import Timer
	print "running fib naive recursion ...",
	sys.stdout.flush()
	t = Timer("fib_rek(32)", "from __main__ import fib_rek")
	print t.timeit(10), "sec"
	print "running fib dynamic implementation (remember values) ...",
	sys.stdout.flush()
	t = Timer("fib_mem(32)", "from __main__ import fib_mem")
	print t.timeit(10), "sec"
	print "running fib moivre-binet formula ...",
	sys.stdout.flush()
	t = Timer("fib_close(32)", "from __main__ import fib_close")
	print t.timeit(10), "sec"
