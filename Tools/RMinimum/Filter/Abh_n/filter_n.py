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

    digits = str(digits)

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    files.remove('filter_n.py')

    N, K, E, V, C, L = [], [], [[], [], []], [[], [], []], [4, 32, 256], []
    for j in range(len(C)):
        for i in range(len(files)):
            algo, filter, n, k, rest = files[i].split('_')
            if int(k) == C[j]:
                df = pd.read_csv(files[i])
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

                E[j].append(e)
                V[j].append(v)

                plt.plot(x, y / s, '-o', label = 'log2(n) = ' + str(n)) #, label='log2(n) | E | V : ' + str(n) + ' | ' + str(e) + ' | ' + str(10000*v))

        #plt.title('k(n) = ' + str(C[j]), fontsize=20)
        plt.xlabel("ΔW",  fontsize=18)
        plt.ylabel('h(n)',  fontsize=18)
        plt.legend(loc='upper right')
        plt.gcf()
        plt.savefig('Plot/min_filter_D_n_' + str(C[j]) + '.png', bbox_inches='tight')
        plt.clf()
    N = sorted(list(set(N)))
    K = sorted(list(set(K)))

    #   Erwartungswert
    for i in range(len(E)):
        plt.plot(N, E[i], '-o', label='log2(k) = ' + str(K[i]))
    plt.xlabel("n",  fontsize=18)
    plt.ylabel('µ',  fontsize=18)
    plt.xscale('log', basex =2)
    plt.legend(loc='center right')
    plt.gcf()
    plt.savefig('Plot/min_filter_E_n.png', bbox_inches='tight')
    plt.xscale('linear')
    plt.clf()

    #   Varianz
    for i in range(len(V)):
        plt.plot(N, V[i], '-o', label='log2(k) = ' + str(K[i]))
    plt.xlabel("n",  fontsize=18)
    plt.ylabel('V(n)',  fontsize=18)
    plt.xscale('log', basex= 2)
    plt.legend(loc='upper right')
    plt.gcf()
    plt.savefig('Plot/min_filter_V_n.png', bbox_inches='tight')
    plt.xscale('linear')
    plt.clf()

    #   log
    for i in range(len(V)):
        N_log = []
        for j in range(len(N)):
            N_log.append(math.log(N[j], 2))
        plt.plot(N_log, V[i], '-o', label = 'log2(k) = ' + str(K[i]))
    plt.xlabel("log2(n)",  fontsize=18)
    plt.ylabel('V(n)',  fontsize=18)
    plt.legend(loc='upper right')
    plt.gcf()
    plt.savefig('Plot/min_filter_V_n_log.png', bbox_inches='tight')
    plt.clf()

    #   loglog
    for i in range(len(V)):
        N_loglog = []
        for j in range(len(N)):
            N_loglog.append(math.log(math.log(N[j], 2), 2))
        plt.plot(N_loglog, V[i], '-o', label = 'log2(k) = ' + str(K[i]))
    plt.xlabel("log2log2(n)",  fontsize=18)
    plt.ylabel('V(n)',  fontsize=18)
    plt.legend(loc='upper right')
    plt.gcf()
    plt.savefig('Plot/min_filter_V_n_loglog.png', bbox_inches='tight')
    plt.clf()

    #   logloglog
    for i in range(len(V)):
        N_logloglog = []
        for j in range(len(N)):
            N_logloglog.append(math.log(math.log(N[j], 2), 2))
        V_s = []
        for j in range(len(V[i])):
            V_s.append(100*V[i][j])
        plt.plot(N_logloglog, V_s, '-o', label = 'log2(k) = ' + str(K[i]))
    plt.xlabel("log2log2log2(n)",  fontsize=18)
    plt.ylabel('V(n)',  fontsize=18)
    plt.legend(loc='upper right')
    plt.gcf()
    plt.savefig('Plot/min_filter_V_n_S.png', bbox_inches='tight')
    plt.clf()


    E_100   = [[], [], []]
    E_1000  = [[], [], []]
    E_10000 = [[], [], []]
    V_100   = [[], [], []]
    V_1000  = [[], [], []]
    V_10000 = [[], [], []]


    for i in range(3):
        for j in range(len(E[i])):
            E_100[i].append(100 * E[i][j])
            E_1000[i].append(1000 * E[i][j])
            E_10000[i].append(10000 * E[i][j])
            V_100[i].append(100 * V[i][j])
            V_1000[i].append(1000 * V[i][j])
            V_10000[i].append(10000 * V[i][j])




    dfout = pd.DataFrame(data={'n': N, 'E': E[0], 'V': V[0],
                                'E_100': E_100[0], 'E_1000': E_1000[0], 'E_10000': E_10000[0],
                                'V_100': V_100[0], 'V_1000': V_1000[0], 'V_10000': V_10000[0], })
    dfout = dfout.sort_values(by=['n'])
    dfout.to_csv('Fit/filter_E_V_n_csv.csv')

    dfout4   = pd.DataFrame(data={'n': N, 'V': V[0]})
    dfout32  = pd.DataFrame(data={'n': N, 'V': V[1]})
    dfout256 = pd.DataFrame(data={'n': N, 'V': V[2]})
    dfout4  = dfout4.sort_values(by=['n'])
    dfout32  = dfout32.sort_values(by=['n'])
    dfout256 = dfout256.sort_values(by=['n'])
    dfout4.to_csv('Fit/filter_V4_n_csv.csv')
    dfout32.to_csv('Fit/filter_V32_n_csv.csv')
    dfout256.to_csv('Fit/filter_V256_n_csv.csv')
    return
# ==================================================

#data(0, [2, 4, 8, 16])
data()