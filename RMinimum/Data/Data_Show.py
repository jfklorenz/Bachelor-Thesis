#!/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import glob2


def data_show():

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    files.remove('Data_Show.py')
    print('')
    print('         DATA SHOW')
    print('')
    print('')
    rat = [.68,.51,.33,.16,.99,.82,.49,.32,.16,1,.84,.68]
    res = []

    for i in range(len(files)):
        df = pd.read_csv(files[i])
        algo, n, k, rest = files[i].split('_')

        res.append([n, k, df['min'].mean(), df['rem'].mean(), df['work'].mean(), df['Rec'].mean()])

    pairs = []
    for i in range(len(res)):
        pair = []
        v = False
        for j in range(len(res)):
            if i + 6 == int(res[j][0]):
                pair.append(res[j])
                v = True
        if v:
            pairs.append(pair)

    for a in range(len(pairs)):
        for b in range(2):
            for c in range(2,6):
                pairs[a][b][c] = round(pairs[a][b][c], 2)


    for i in range(len(pairs)):
        print('n | k1 | k2 :', pairs[i][0][0], '|', pairs[i][0][1], '|', pairs[i][1][1])
        print('--------------------------------------------')
        print('1   min | rem :', pairs[i][0][2], '|', pairs[i][0][3])
        print('2   min | rem :', pairs[i][1][2], '|', pairs[i][1][3])
        print('X   min | rem :', round(rat[i]*pairs[i][0][2] + (1 - rat[i])*pairs[i][1][2],2), '|', round(rat[i]*pairs[i][0][3] + (1 - rat[i])*pairs[i][1][3],2))
        print('--------------------------------------------')
        print('')
        print('')



    return

data_show()