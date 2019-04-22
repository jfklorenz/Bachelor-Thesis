#!/usr/bin/python3
# ==================================================
"""
File: RMedian - Graphic Generator - Theorem 28
Author: Julian Lorenz
"""
# ==================================================
#   Import
import pandas as pd
import matplotlib.pyplot as plt
import os
import math


# ==================================================
def data():
    cases = ['Plot', 'Fit']
    for case in cases:
        if not os.path.exists(case):
            os.makedirs(case)
    if not os.path.exists('Fit'):
        os.makedirs('Plot')

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print(files)
    files.remove('med_theo28.py')

    fig, ax = plt.subplots(1)

    N, K, D, FM, FR, W, REC, CASE, MINC, RES = [], [], [], [], [], [], [], [], [], []
    for f in range(len(files)):
        name, rep = files[f].split('__')
        algo, type, n, k, d = name.split('_')

        df = pd.read_csv(files[f])
        df0 = df['rat'].value_counts().to_frame().reset_index().rename(columns={'index': 'rat', 'rat': 'count'})
        df0 = df0.sort_values(by=['rat'])
        df00 = df0
        dfr = pd.read_csv(files[f])
        dfr['rat'] = dfr['rat'].apply(lambda x:round(x,3))

        dfr0 = dfr['rat'].value_counts().to_frame().reset_index().rename(columns={'index': 'rat', 'rat': 'count'})
        dfr0 = dfr0.sort_values(by=['rat'])

        x = df0['rat']  # in percentage
        y = df0['count']



        df1 = df['case'].value_counts().to_frame().reset_index().rename(columns={'index': 'case', 'case': 'count'})
        df1 = df1.sort_values(by=['case'])

        xr = dfr0['rat']
        yr = dfr0['count']
        s = sum(yr)
        N.append(2 ** int(n))
        K.append(int(k))
        D.append(int(d))
        FM.append(df['med'].mean())
        FR.append(df['rem'].mean())
        W.append(df['work'].mean())
        REC.append(df['rec'].mean())
        CASE.append(df['case'].mean())
        MINC.append(df['MinC'].mean())
        RES.append(df1)

        col = ['b', 'r', 'g', 'y', 'c']

        ax.stem(xr, round(yr / s, 2), markerfmt=col[f] + 'o', basefmt=col[f] + '-',
                linefmt=col[f] + '-')

    # --------------------------------------------------
    #   Distribution
    # plt.title('k(n) = ' + str(C[j]), fontsize=20)
    plt.xlabel("ΔX", fontsize=18)
    plt.ylabel('% runs', fontsize=18)
    #plt.legend(loc='upper right')
    plt.gcf()
    plt.savefig('Plot/med_theo28_filter.png', bbox_inches='tight')
    plt.clf()

    ExM, ExR, ExW = [], [], []

    for n in N:
        ExM.append(math.log(math.log(n, 2), 2))
        ExR.append(n ** (1 / 2))
        ExW.append(n)

    # --------------------------------------------------
    #   MEDIAN
    plt.plot(N, FM, '-o', label='f_med(n)')
    plt.plot(N, ExM, '-o', label='loglog(n)')

    plt.xlabel("n", fontsize=18)
    plt.ylabel('f_med', fontsize=18)
    plt.legend(loc='upper left')
    plt.gcf()
    plt.savefig('Plot/med_algo_theo28_med.png', bbox_inches='tight')
    plt.clf()

    # --------------------------------------------------
    #   MEDIAN
    N2 = [math.log(math.log(n), 2) for n in N]
    plt.plot(N2, FM, '-o', label='f_med(n)')
    plt.plot(N2, ExM, '-o', label='loglog(n)')

    plt.xlabel("n", fontsize=18)
    plt.ylabel('f_med', fontsize=18)
    plt.legend(loc='upper left')
    plt.gcf()
    plt.savefig('Plot/med_algo_theo28_med_logscale.png', bbox_inches='tight')
    plt.clf()


    # --------------------------------------------------
    #   REMAINING
    plt.plot(N, FR, '-o', label='f_rem(n)')
    plt.plot(N, ExR, '-o', label='n^(1/2)')

    plt.xlabel("n", fontsize=18)
    plt.ylabel('f_rem', fontsize=18)
    plt.legend(loc='upper left')
    plt.gcf()
    plt.savefig('Plot/med_algo_theo28_rem.png', bbox_inches='tight')
    plt.clf()

    # --------------------------------------------------
    #   Work
    plt.plot(N, W, '-o', label='w(n)')
    plt.plot(N, ExW, '-o', label='n')

    plt.xlabel("n", fontsize=18)
    plt.ylabel('work', fontsize=18)
    plt.legend(loc='upper left')
    plt.gcf()
    plt.savefig('Plot/med_algo_theo28_work.png', bbox_inches='tight')
    plt.clf()

    # --------------------------------------------------
    #   CASE
    plt.plot(N, CASE, '-o', label='outcome')
    plt.xlabel("n", fontsize=18)
    plt.ylabel('AKS = 1; DET = 0', fontsize=18)
    plt.legend(loc='upper left')
    plt.gcf()
    plt.savefig('Plot/med_algo_theo28_case.png', bbox_inches='tight')
    plt.clf()

    # --------------------------------------------------
    #   CSV
    dfout = pd.DataFrame(data={'n': N, 'med': FM, 'rem': FR, 'work': W})
    dfout = dfout.sort_values(by=['n'])
    dfout.to_csv('Fit/med_algo_theo28_data.csv')

    return


# ==================================================

data()
