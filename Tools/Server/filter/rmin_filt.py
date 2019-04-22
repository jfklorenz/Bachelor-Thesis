#!/bin/python3
# ==================================================
#   Import
import math
import random
import queue
import pandas

# ==================================================
def rminimum(X,k, dig):
    k = int(k)
    n = len(X)

    W, L = RMinimum_step1(X)
    minele = RMinimum_step2(L, k)
    res3 = RMinimum_step3(W, k, minele)

    rat0 = len(res3)/n
    rat1 = round(len(res3)/n, 2)
    rat2 = round(len(res3)/n, 4)
    rat3 = round(len(res3)/n, 8)

    rat = [len(res3)/n]
    if dig == 0:
        for i in range(1, 10):
            rat.append(round(len(res3)/n, i))
    else:
        for d in dig:
            rat.append(round(len(res3)/n, d))
    return rat

# ==================================================
def RMinimum_step1(lst):

    random.shuffle(lst)

    W = [0 for _ in range(len(lst) // 2)]
    L = [0 for _ in range(len(lst) // 2)]

    for i in range(len(lst) // 2):
        if lst[2 * i] > lst[2 * i + 1]:
            W[i] = lst[2 * i + 1]
            L[i] = lst[2 * i]
        else:
            W[i] = lst[2 * i]
            L[i] = lst[2 * i + 1]


    return W, L

# ==================================================
def RMinimum_step2(L, k):

    random.shuffle(L)
    res = [L[i * k:(i + 1) * k] for i in range((len(L) + k - 1) // k)]
    minele = [0 for _ in range(len(res))]

    var = list(res)
    for i in range(len(var)):
        q = queue.Queue()

        for item in var[i]:
            q.put(item)

        while q.qsize() > 1:
            a = q.get()
            b = q.get()

            if a < b:
                q.put(a)
            else:
                q.put(b)

        minele[i] = q.get()

    return minele

# ==================================================
def RMinimum_step3(lst, k, minele):

    random.shuffle(lst)
    var = [lst[i * k:(i + 1) * k] for i in range((len(lst) + k - 1) // k)]
    res = [0 for _ in range(len(var))]

    for i in range(len(var)):
        res[i] = [elem for elem in var[i] if elem < minele[i]]

    res = [item for sublist in res for item in sublist]

    return res

# ==================================================

def run(n, k, rep = 1000, dig = 0):

    rat = [[] for _ in range(10)]
    for r in range(rep):
        X = [i for i in range(n)]
        ra = rminimum(X, k, dig)

        if dig == 0:
            for i in range(10):
                rat[i].append(ra[i])
        else:
            for i in range(len(dig) + 1):
                rat[i].append(ra[i])


    n = str(int(math.log(n) / math.log(2)))
    if len(n) == 1:
        n = '0' + n

    keys = []
    if dig == 0:
        for i in range(10):
            keys.append(str(i))
    else:
        for i in range(len(dig) + 1):
            keys.append(str(i))

    dic = dict(zip(keys, rat))

    x = str(random.randint(1000,9999))
    filename0 = "./min_filter_" + n + "_" + str(int(k)) + '_' + str(rep) + '__' + x + ".csv"
    df0 = pandas.DataFrame(data=dic)

    df0.to_csv(filename0, sep=',',index=False)
    return

# ==================================================
