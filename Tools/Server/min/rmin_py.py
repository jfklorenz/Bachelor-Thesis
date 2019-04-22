#!/bin/python3
# ==================================================
#   Import
import math
import random
import queue
import pandas

# ==================================================
def rminimum(X,k, cnt = [], rec = 0):
    k = int(k)
    n = len(X)
    if cnt == []:
        cnt = [0 for _ in range(len(X))]

    if len(X) == 3:
        random.shuffle(X)
        if X[0] < X[1]:
            cnt[X[0]] += 2
            cnt[X[1]] += 1
            cnt[X[2]] += 1

            if X[0] < X[2]:
                X = X[0]
            else:
                X = X[2]

        else:
            cnt[X[0]] += 1
            cnt[X[1]] += 2
            cnt[X[2]] += 1

            if X[1] < X[2]:
                X = X[1]
            else:
                X = X[2]

        return cnt

    W, L, cnt = RMinimum_step1(X, cnt)
    minele, cnt = RMinimum_step2(L, k, cnt)
    res3, cnt = RMinimum_step3(W, k, minele, cnt)
    res4, cnt, rec = RMinimum_step4(res3, k, n, cnt, rec)

    return cnt, rec

# ==================================================
def RMinimum_step1(lst, cnt):

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
        cnt[lst[2 * i + 1]] += 1
        cnt[lst[2 * i]] += 1

    return W, L, cnt

# ==================================================
def RMinimum_step2(L, k, cnt):

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
            cnt[a] += 1
            cnt[b] += 1
        minele[i] = q.get()

    return minele, cnt

# ==================================================
def RMinimum_step3(lst, k, minele, cnt):

    random.shuffle(lst)
    var = [lst[i * k:(i + 1) * k] for i in range((len(lst) + k - 1) // k)]
    res = [0 for _ in range(len(var))]

    for i in range(len(var)):
        res[i] = [elem for elem in var[i] if elem < minele[i]]
        cnt[minele[i]] += len(var[i])
        for elem in var[i]:
            cnt[elem] += 1

    res = [item for sublist in res for item in sublist]

    return res, cnt

# ==================================================
def RMinimum_step4(newW, k, n, cnt, rec):

    if len(newW) <= (math.log(n)/math.log(2))**2:   # log^2(n) vs log(n)
        q = queue.Queue()

        var = list(newW)
        for item in var:
            q.put(item)
        while q.qsize() > 1:
            a = q.get()
            b = q.get()

            if a < b:
                q.put(a)
            else:
                q.put(b)

            cnt[a] += 1
            cnt[b] += 1
        res = q.get()

    else:
        rec += 1
        res = rminimum(newW,k, cnt, rec)

    return res, cnt, rec

# ==================================================
def run(n, k, rep = 1000):
    mini = []
    rem = []
    fgc = []
    work = []
    recl = []
    for r in range(rep):
        X = [i for i in range(n)]
        cnt, rec = rminimum(X, k)

        mini.append(cnt[0])
        rem.append(max(cnt[1:]))
        fgc.append(max(cnt))
        work.append(int(sum(cnt)/2))
        recl.append(rec)

    n = str(int(math.log(n) / math.log(2)))
    if len(n) == 1:
        n = '0' + n
    x = str(random.randint(1000,9999))
    filename = "./min_algo_" + n + "_" + str(int(k)) + "_" + str(rep) + "__" + x + ".csv"
    df = pandas.DataFrame(data={"min": mini, "rem": rem, "fgc":fgc, "work": work, "rec": recl})
    df.to_csv(filename, sep=',',index=False)
    return

# ==================================================