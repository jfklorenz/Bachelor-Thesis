#!/bin/python3
# ==================================================
#   Import
import math
from rmin_py import run

# ==================================================
#   Theo 5
nlst = [22]

# ==================================================
for n in nlst:
    k = n / math.log(n, 2)
    k0 = math.floor(k)
    k1 = math.ceil(k)

    run(2**n, int(k1))


