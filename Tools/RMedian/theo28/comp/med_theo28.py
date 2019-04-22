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
    cases = ['Plot']
    for case in cases:
        if not os.path.exists(case):
            os.makedirs(case)

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print(files)
    files.remove('med_theo28.py')

    fig, ax = plt.subplots(1)

    nl, kl, dfl, dl = [], [], [], []
    for i in range(len(files)):
        name, rep = files[i].split('__')
        algo, type, n, k, d = name.split('_')
        nl.append(2**int(n))
        kl.append(int(k))
        dl.append(int(d))
        df = pd.read_csv(files[i], sep=",", )
        dfl.append(df)

    d0 = pd.DataFrame()
    d0[dl[0]] = dfl[0]['med']
    d0[dl[1]] = dfl[1]['med']

    plt.xlabel("d", fontsize=18)
    plt.ylabel('f_med', fontsize=18)
    #plt.legend(loc='upper left')
    boxplot = d0.boxplot(column=[dl[0], dl[1]])
    plt.gcf()
    plt.savefig('Plot/med_algo_theo28_comp_med.png', bbox_inches='tight')
    plt.clf()


    d0 = pd.DataFrame()
    d0[dl[0]] = dfl[0]['rem']
    d0[dl[1]] = dfl[1]['rem']

    plt.xlabel("d", fontsize=18)
    plt.ylabel('f_rem', fontsize=18)
    #plt.legend(loc='upper left')
    boxplot = d0.boxplot(column=[dl[0], dl[1]])
    plt.gcf()
    plt.savefig('Plot/med_algo_theo28_comp_rem.png', bbox_inches='tight')
    plt.clf()



    d0 = pd.DataFrame()
    d0[dl[0]] = dfl[0]['work']
    d0[dl[1]] = dfl[1]['work']

    plt.xlabel("d", fontsize=18)
    plt.ylabel('work', fontsize=18)
    #plt.legend(loc='upper left')
    boxplot = d0.boxplot(column=[dl[0], dl[1]])
    plt.gcf()
    plt.savefig('Plot/med_algo_theo28_comp_work.png', bbox_inches='tight')
    plt.clf()






    #plt.boxplot(dfl[0]["work"])
    #plt.boxplot(dfl[1]["work"])
    #plt.show()
    # --------------------------------------------------
    #   Compare MEDIAN


    return


# ==================================================

data()
