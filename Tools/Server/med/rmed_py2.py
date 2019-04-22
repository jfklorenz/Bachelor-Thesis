#!/bin/python3
# ==================================================
#   Import
from rmed_algo import run

nlst = [2**19+1]

for n in nlst:
	k = int(n ** (2 / 3))
	d = int(n ** (1 / 12))
	run(n, k, d, 5)
