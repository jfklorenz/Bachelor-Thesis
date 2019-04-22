#!/usr/bin/python3
# ==================================================
"""
File: RMedian - Full Algorithm
Author: Julian Lorenz
"""
# ==================================================
#   Import
import math
import random
import statistics
import pandas

# ==================================================
#   RMedian
def rmedian(X, k, d, cnt = [], rec = 0, n0 = 0):
    rmed = statistics.median(X)
    if rec == 0:
        n0 = len(X)

    if cnt == []:
        cnt = [0 for _ in range(len(X))]

    S, XS, L, C, R = phase1(X, k, d)
    S, XS, L, C, R, cnt = phase2(S, XS, L, C, R, cnt)

    MinC = True
    if not rmed in C:
        MinC = False
    rat = len(C) / n0

    return rat, MinC

# ==================================================
#   Phase 1
def phase1(X, k, d):
    #   Initiation
    n = len(X)
    random.shuffle(X)
    S = X[:k]
    XS = X[k:]
    S.sort()

    #   Keeping the list entries below k/2
    if 2*(k*math.log2(n))**0.5 < k/2:
        lst = [2*(k*math.log2(n))**0.5]
        if 3*(k*math.log2(n))**0.5 < k/2:
            lst.append(3*(k*math.log2(n))**0.5)
            while d*lst[len(lst) - 1] < k/2:
                lst.append(d*lst[len(lst) - 1])
        lst.append(k/2)
    else:
        lst = [k/2]

    #   Buckets
    L = [[] for _ in range(len(lst) - 1)]
    R = [[] for _ in range(len(lst) - 1)]
    C = []

    for s in S[math.floor(k / 2 - lst[0]): math.ceil(k / 2 + lst[0])]:
        C.append(s)

    for i in range(1, len(lst)):
        for s in S[math.floor(k / 2 - lst[i]): math.floor(k / 2 - lst[i - 1])]:
            L[i - 1].append(s)
        for s in S[math.ceil(k / 2 + lst[i - 1]): math.ceil(k / 2 + lst[i])]:
            R[i - 1].append(s)

    return S, XS, L, C, R

# ==================================================
#   Phase 2
def phase2(S, XS, L, C, R, cnt):
    mark = [False for _ in range(2 ** 28)]
    b = len(L)

    random.shuffle(XS)
    for x_i in XS:
        med = 0
        for j in reversed(range(0, b - 1)):

            current = 2 ** 50
            random.shuffle(L[j])
            for l in L[j]:
                if cnt[l] < current:
                    x_A = l

            if mark[x_A] == True:
                c = 1

            else:
                c = 2

            cnt[x_i] += 1
            cnt[x_A] += 1

            if x_i < x_A:
                if j + c < b:
                    mark[x_i] = True
                    L[j + c].append(x_i)
                    med = -1
                else:
                    med = -2
                break

            current2 = 2 ** 50
            random.shuffle(R[j])
            for r in R[j]:
                if cnt[r] < current2:
                    x_B = r

            if mark[x_B] == True:
                c = 1
            else:
                c = 2

            cnt[x_i] += 1
            cnt[x_B] += 1

            if x_i > x_B:
                if j + c < b:
                    mark[x_i] = True
                    R[j + c].append(x_i)
                    med = 1
                else:
                    med = 2
                break
        if med == 0:
            C.append(x_i)
        elif med == -2:
            L[len(L) - 1].append(x_i)
        elif med == 2:
            R[len(R) - 1].append(x_i)
    return S, XS, L, C, R, cnt

# ==================================================
def run(n, k, d, rep = 100):
    ratl = []
    MinCl = []
    for r in range(rep):
        X = [i for i in range(n)]
        rat, MinC = rmedian(X, k, d)
        ratl.append(rat)
        MinCl.append(MinC)

    n = str(int(math.log(n, 2)))
    if len(n) == 1:
        n = '0' + n
    x = str(random.randint(1000,9999))
    filename = "./med_filt_" + n + "_" + str(int(k)) + "_" + str(int(d)) + "_" + str(rep) + "__" + x + ".csv"
    df = pandas.DataFrame(data={"med": ratl, "MinC": MinCl})
    df.to_csv(filename, sep=',',index=False)
    return