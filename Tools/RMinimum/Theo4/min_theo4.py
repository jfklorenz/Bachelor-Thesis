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
    files.remove('min_theo4.py')

    N, K, EPS, FGC, MIN, REM, WORK, REC = [], [], 0, [], [], [], [], []
    for i in range(len(files)):
        algo, filter, n, k, rest = files[i].split('_')
        df = pd.read_csv(files[i])
        N.append(2**int(n))
        K.append(int(k))
        EPS = math.log(int(K[0]), 2) / math.log(int(N[0]), 2)
        FGC.append(df['fgc'].mean())
        MIN.append(df['min'].mean())
        REM.append(df['rem'].mean())
        WORK.append(df['work'].mean())
        REC.append(df['rec'].mean())

    EPS2 = 0
    for j in range(1, 13):
        if 1/j == EPS:
            EPS2 = str(j)

    # ============================================================
    #   MIN
    plt.plot(N, MIN, '-o', label='f_min(n)')
    plt.xlabel("n", fontsize=18)
    plt.xscale('log', basex=2)
    plt.ylabel('f_min(n)', fontsize=18)
    plt.legend(loc='upper left')
    plt.gcf()
    plt.savefig('Plot/min_theo4_' + str(EPS2) + '_min.png', bbox_inches='tight')
    plt.clf()

    #   Theo4
    plt.plot(N, MIN, '-o', label='f_min(n)')
    theo4_fgm = []
    for i in range(len(N)):
        theo4_fgm.append(EPS ** (-1) * math.log(math.log(N[i], 2), 2))
    plt.plot(N, theo4_fgm, '-o', label='Theorem 4: O( ' + EPS2 + '^(-1) * log2log2(n) )')
    plt.xlabel("n", fontsize=18)
    plt.xscale('log', basex=2)
    plt.ylabel('f', fontsize=18)
    plt.legend(loc='upper left')
    plt.gcf()
    plt.savefig('Plot/min_theo4_' + str(EPS2) + '_min_pred.png', bbox_inches='tight')
    plt.clf()

    # ============================================================
    #   REM
    plt.plot(N, REM, '-o', label='f_rem(n)')
    plt.xlabel("n", fontsize=18)
    plt.xscale('log', basex=2)
    plt.ylabel('f_rem', fontsize=18)
    plt.legend(loc='upper left')
    plt.gcf()
    plt.savefig('Plot/min_theo4_' + str(EPS2) + '_rem.png', bbox_inches='tight')
    plt.clf()

    #   Theo4
    plt.plot(N, REM, '-o', label='f_rem(n)')
    theo4_fgr = []
    for i in range(len(N)):
        theo4_fgr.append(N[i]**EPS)
    plt.plot(N, theo4_fgr, '-o', label='Theorem 4: O( n^(1 / ' + EPS2 + ' )')
    plt.xlabel("n", fontsize=18)
    plt.xscale('log', basex=2)
    plt.ylabel('f', fontsize=18)
    plt.legend(loc='upper left')
    plt.gcf()
    plt.savefig('Plot/min_theo4_' + str(EPS2) + '_rem_pred.png', bbox_inches='tight')
    plt.clf()

    # ============================================================
    #   FGC
    plt.plot(N, FGC, '-o', label='f(n)')
    plt.xlabel("n", fontsize=18)
    plt.xscale('log', basex=2)
    plt.ylabel('f(n)', fontsize=18)
    plt.legend(loc='upper left')
    plt.gcf()
    plt.savefig('Plot/min_theo4_' + str(EPS2) + '_fgc.png', bbox_inches='tight')
    plt.clf()

    # ============================================================
    #   WORK
    plt.plot(N, WORK, '-o', label='w(n)')
    plt.xlabel("n", fontsize=18)
    plt.xscale('log', basex=2)
    plt.ylabel('w(n)', fontsize=18)
    plt.yscale('log', basey=2)
    plt.legend(loc='upper left')
    plt.gcf()
    plt.savefig('Plot/min_theo4_' + str(EPS2) + '_work.png', bbox_inches='tight')
    plt.clf()

    #   Theo 3
    plt.plot(N, WORK, '-o', label='w(n)')
    theo3 = []
    for n in N:
        theo3.append(n)
    plt.plot(N, theo3, '-o', label='Theorem 3: O(n)')
    plt.xlabel("n", fontsize=18)
    plt.xscale('log', basex=2)
    plt.ylabel('w(n)', fontsize=18)
    plt.yscale('log', basey=2)
    plt.legend(loc='upper left')
    plt.gcf()
    plt.savefig('Plot/min_theo4_' + str(EPS2) + '_work.png', bbox_inches='tight')
    plt.clf()

    # ============================================================
    #   REC
    plt.plot(N, REC, '-o', label='rec(n)')
    plt.xlabel("n", fontsize=18)
    plt.xscale('log', basex=2)
    plt.ylabel('rec(n)', fontsize=18)
    plt.legend(loc='upper left')
    plt.gcf()
    plt.savefig('Plot/min_theo4_' + str(EPS2) + '_rec.png', bbox_inches='tight')
    plt.clf()

    # ============================================================
    #   DATA
    dfout = pd.DataFrame(data={'n': N, 'k': K, 'fgc': FGC, 'min': MIN, 'rem': REM, 'work': WORK, 'rec': REC})
    dfout = dfout.sort_values(by=['n'])
    dfout.to_csv('Fit/min_fit_theo4.csv')

    dfoutm = pd.DataFrame(data={'n': N, 'k': K, 'min': MIN})
    dfoutm = dfoutm.sort_values(by=['n'])
    dfoutm.to_csv('Fit/min_fit_theo4_min.csv')

    dfoutr = pd.DataFrame(data={'n': N, 'k': K, 'rem': REM})
    dfoutr = dfoutr.sort_values(by=['n'])
    dfoutr.to_csv('Fit/min_fit_theo4_rem.csv')

    return
# ==================================================

#data(0, [2, 4, 8, 16])
data()