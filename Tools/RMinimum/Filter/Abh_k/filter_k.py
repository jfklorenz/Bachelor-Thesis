#!/usr/bin/python3
# ==================================================
"""
File: RMinimum - Phase 0
Author: Julian Lorenz
"""
# ==================================================
#   Import
import pandas as pd
import matplotlib.pyplot as plt
import os
import math

# ==================================================
def data(digits = 0, lst = [], dat = 1, pic = 1):

    cases = ['Plot', 'Fit']
    for case in cases:
        if not os.path.exists(case):
            os.makedirs(case)
    if not os.path.exists('Fit'):
        os.makedirs('Plot')
    fig, ax = plt.subplots(1)
    digits = str(digits)
    plt.ylim(0, 0.009)
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    files.remove('filter_k.py')

    N, K, E, V, C, L = [], [] , [], [], [], []
    for f in range(len(files)):
        algo, filter, n, k, rest = files[f].split('_')

        df = pd.read_csv(files[f])
        df0 = df[digits].value_counts().to_frame().reset_index().rename(columns={'index': digits, digits: 'count'})
        df0 = df0.sort_values(by=[digits])

        x = df0[digits] # in percentage
        y = df0['count']
        s = sum(y)

        N.append(2**int(n))
        K.append(int(k))
        e = 0
        for i in range(len(x)):
            e += x[i] * y[i]
        e = e / s
        v = 0
        for i in range(len(x)):
            v += (y[i] / s) * (x[i] - e)**2

        E.append(e)
        V.append(v)

        q = 6 - len(str(round(e, 4)))
        qc = q * '0'

        if int(k) <= 64:
            col = ['b', 'r', 'g', 'k', 'y', 'c', 'b', 'r', 'g', 'k', 'y', 'c', 'b', 'r', 'g', 'k', 'y', 'c']
            ax.stem(x, y/s, markerfmt= col[f] + 'o', basefmt= col[f] + '-',
                            linefmt= col[f] + '-',
                            label = '(' + str(f+1) + ') :   ' +
                                    ' E[ΔW] = ' + str(round(e, 4)) + qc +
                                    ',   V[ΔW] = ' + str(round(1000000*v, 3)) + 'e-06'
                            )
    plt.xlabel("ΔW",  fontsize=18)
    plt.ylabel('h(n)',  fontsize=18)
    plt.legend(loc='upper center')
    plt.gcf()
    plt.savefig('Plot/min_filter_D_k.png', bbox_inches='tight')
    plt.clf()
    N = sorted(list(set(N)))
    K = sorted(list(set(K)))

    #   Erwartungswert
    for i in range(len(E)):
        plt.plot(K, E, '-o', label='log2(n) = ' + str(K[i]))
    plt.xlabel("k",  fontsize=18)
    plt.ylabel('µ',  fontsize=18)
    plt.xscale('log', basex =2)
    plt.legend(loc='upper right')
    plt.gcf()
    plt.savefig('Plot/min_filter_E_k.png', bbox_inches='tight')
    plt.xscale('linear')
    plt.clf()

    #   Varianz
    for i in range(len(V)):
        plt.plot(K, V, '-o', label='log2(n) = ' + str(K[i]))
    plt.yscale('log')
    plt.xlabel("k",  fontsize=18)
    plt.ylabel('V(n)',  fontsize=18)
    plt.xscale('log', basex= 2)
    plt.legend(loc='lower right')
    plt.gcf()
    plt.savefig('Plot/min_filter_V_k.png', bbox_inches='tight')
    plt.xscale('linear')
    plt.clf()

    #   log
    for i in range(len(V)):
        N_log = []
        for j in range(len(K)):
            N_log.append(math.log(K[j], 2))
        plt.plot(N_log, V, '-o', label = 'log2(n) = ' + str(K[i]))
    plt.yscale('log')
    plt.xlabel("log2(k)",  fontsize=18)
    plt.ylabel('V(n)',  fontsize=18)
    plt.legend(loc='lower right')
    plt.gcf()
    plt.savefig('Plot/min_filter_V_k_log.png', bbox_inches='tight')
    plt.clf()

    #   loglog
    for i in range(len(V)):
        N_loglog = []
        for j in range(len(K)):
            N_loglog.append(math.log(math.log(K[j], 2), 2))
        plt.plot(N_loglog, V, '-o', label = 'log2(n) = ' + str(K[i]))
    plt.yscale('log')
    plt.xlabel("log2log2(k)",  fontsize=18)
    plt.ylabel('V(n)',  fontsize=18)
    plt.legend(loc='lower right')
    plt.gcf()
    plt.savefig('Plot/min_filter_V_k_loglog.png', bbox_inches='tight')
    plt.clf()

    #   logloglog
    for i in range(len(V)):
        N_logloglog = []
        for j in range(len(K)):
            N_logloglog.append(math.log(math.log(K[j], 2), 2))
        V_s = []
        for j in range(len(V)):
            V_s.append(100*V[j])
        plt.plot(N_logloglog, V_s, '-o', label = 'log2(n) = ' + str(K[i]))
    plt.yscale('log')
    plt.xlabel("log2log2log2(k)",  fontsize=18)
    plt.ylabel('V(n)',  fontsize=18)
    plt.legend(loc='lower right')
    plt.gcf()
    plt.savefig('Plot/min_filter_V_k_S.png', bbox_inches='tight')
    plt.clf()


    dfout = pd.DataFrame(data={'k': K, 'E': E, 'V': V})
    dfout = dfout.sort_values(by=['k'])
    dfout.to_csv('Fit/min_filter_E_V_k_csv.csv')



    return
# ==================================================

#data(0, [2, 4, 8, 16])
data()