#!/bin/python3
# ==================================================
#   Import
from rmed_algo99 import run

nlst = [2**14 + 1]

for n in nlst:
	k = int(n ** (2 / 3))
	d = int(n ** (1 / 12))
	run(n, k, d, 1000)
