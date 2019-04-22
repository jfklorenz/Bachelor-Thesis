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
def data():
    """
    Generates GNU data files and plots.
    :param case: 0: weighed, 1: ceiled, 3: floored
    :return:
    """

    if not os.path.exists('Plot'):
        os.makedirs('Plot')
    if not os.path.exists('Fit'):
        os.makedirs('Fit')

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    files.remove('min_theo5.py')

    data, data_c, data_f, data_w = [], [], [], []
    for i in range(len(files)):
        name, algo, n, k, rest = files[i].split('_')
        df = pd.read_csv(files[i])

        # 0: n, 1: k, 2: data list
        data.append([2**int(n), float(k), df['fgc'].mean(), df['min'].mean(), df['rec'].mean(), df['rem'].mean(), df['work'].mean()])
    for i in range(20):
        if i % 2 == 0:
            data_f.append(data[i])
        elif i % 2 == 1:
            data_c.append(data[i])
    data_f.append(data[20])
    data_c.append(data[20])
    for i in range(21, 29):
        if i % 2 == 0:
            data_f.append(data[i])
        elif i % 2 == 1:
            data_c.append(data[i])

    for i in range(len(data_c)):
        k = math.log(data_c[i][0], 2) / math.log(math.log(data_c[i][0], 2))
        kc = math.ceil(k)
        kf = math.floor(k)

        v = [data_c[i][0], k]
        for j in range(2, 7):
            v.append((kc - k) * data_f[i][j] + (k - kf) * data_c[i][j])

        data_w.append(v)

    final = [[[] for _ in range(7)] for i in range(3)]

    for i in range(len(data_c)):
        for j in range(7):
            final[0][j].append(data_c[i][j])
            final[1][j].append(data_f[i][j])

    for i in range(len(data_w)):
        for j in range(7):
            final[2][j].append(data_w[i][j])

    lst_data = ['ceil', 'floor', 'weigh']
    lst_case = ['fgc', 'min', 'rec', 'rem', 'work']
    lst_ylabel = ['fragile complexity', 'f_min', '# recursive calls', 'f_rem', 'work']

    for i in range(len(lst_data)):
        dfout = pd.DataFrame(data={'n': final[i][0], 'fgc': final[i][2], 'min': final[i][3], 'rec': final[i][4], 'rem': final[i][5], 'work': final[i][6]})
        dfout = dfout.sort_values(by=['n'])
        dfout.to_csv('Fit/min_theo5_fit_' + lst_data[i] + '_csv.csv')


    for z in [0, 1]:
        for i in range(len(lst_data)):
            for j in range(len(lst_case)):
                plt.clf()
                lbl = ''
                if i == 0:
                    lbl = 'Data: k(n) = ⌈ log2(n) / log2(log2(n)) ⌉'
                elif i == 1:
                    lbl = 'Data: k(n) = ⌊ log2(n) / log2(log2(n)) ⌋'
                elif i == 2:
                    lbl = 'Data: k(n) gewichtet'

                plt.xlabel("n", fontsize=18)
                plt.ylabel(lst_ylabel[j], fontsize=18)
                if z == 1 and (lst_case[j] == 'min' or lst_case[j] == 'rem' or lst_case[j] == 'work'):
                    pred = []
                    if lst_case[j] == 'work':
                        pred = [2**k for k in range(6, 21)]
                        plt.plot(final[i][0], pred, '-o',
                                 label='Theo 5: O(n)')
                        plt.plot(final[i][0], final[i][6], '-o',
                                 label=lbl)
                        plt.legend(loc='upper left', fontsize=12)
                        plt.savefig('Plot/min_theo5_' + lst_case[j] + '_' + lst_data[i] + '_pred.png',
                                    bbox_inches='tight')
                        plt.clf()
                    else:
                        for y in range(2):
                            if y == 0:
                                plt.xlabel("n", fontsize=18)
                                plt.ylabel(lst_ylabel[j], fontsize=18)
                                lst = [[6.97, -9.91], [6.42, -7.88], [7.37, -10.88]]
                                for k in range(6, 21):
                                    a = lst[i][0]
                                    b = lst[i][1]
                                    pred.append(a * k / math.log(k, 2) + b)
                                plt.plot(final[i][0], final[i][j + 2], '-o', label=lbl)
                                plt.plot(final[i][0], pred, '-o', label='F(n) = ' + str(a) + ' * log2(n) / log2(log2(n)) - ' + str(-b))
                                plt.legend(loc='lower right', fontsize=12)
                                plt.savefig('Plot/min_theo5_' + lst_case[j] + '_' + lst_data[i] + '_fit.png', bbox_inches='tight')
                                plt.clf()
                            else:
                                pred = []
                                plt.xlabel("n", fontsize=18)
                                plt.ylabel(lst_ylabel[j], fontsize=18)
                                for k in range(6, 21):
                                    pred.append(k / math.log(k, 2))
                                plt.plot(final[i][0], final[i][j + 2], '-o', label=lbl)
                                plt.plot(final[i][0], pred, '-o',
                                         label='Theo 5: O(log2(n) / log2(log2(n)))')
                                plt.legend(loc='center right', fontsize=12)
                                plt.savefig('Plot/min_theo5_' + lst_case[j] + '_' + lst_data[i] + '_pred.png',
                                            bbox_inches='tight')
                                plt.clf()
                else:
                    plt.plot(final[i][0], final[i][j + 2], '-o', label=lbl)
                    if j == 4:
                        plt.legend(loc='upper left', fontsize=12)
                    else:
                        plt.legend(loc='lower right', fontsize=12)
                    plt.savefig('Plot/min_theo5_' + lst_case[j] + '_' + lst_data[i] + '.png', bbox_inches='tight')
                plt.clf()

    plt.plot(final[0][0], final[0][2], '-o', label='Data: ceiled')
    plt.plot(final[1][0], final[1][2], '-o', label='Data: floored')
    plt.plot(final[2][0], final[2][2], '-o', label='Data: weighed')
    lst = [[6.97, -9.91], [6.42, -7.88], [6.66, -8.78]]
    pred = [[],[],[]]
    for i in range(3):
        a = lst[i][0]
        b = lst[i][1]
        for k in range(6, 21):
            pred[i].append(a * k / math.log(k, 2) + b)

    for i in range(3):
        case = ['ceiled', 'floored', 'weighed']
        plt.plot(final[i][0], pred[i], '-o', label='Fit: ' + case[i])

    plt.xlabel("n", fontsize=18)
    plt.ylabel('f_min', fontsize=18)
    plt.legend(loc='lower right', fontsize=14)
    plt.savefig('Plot/min_theo5_min_all.png', bbox_inches='tight')
    plt.clf()




    # ========================================================
    #   Predictions




    return

# ==================================================
data()