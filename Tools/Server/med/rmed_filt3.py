#!/bin/python3
# ==================================================
#   Import
from rmed_filt import run

nlst = [2**20 + 1]

for n in nlst:
	k = int(n ** (2 / 3))
	d = int(n ** (1 / 12))
	run(n, k, d, 5)
