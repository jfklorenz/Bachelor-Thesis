#!/usr/bin/python3

#   Import
import csv
import pandas as pd
import os
import glob2
from math import log2
from pathlib import Path
from shutil import copyfile

# ==================================================



def merge():
    if not os.path.exists('merge'):
        os.makedirs('merge')

    # ----------------------------------------
    #   Read All Files
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    files.remove('merge.py')

    # ----------------------------------------
    #   Move through files in order
    while len(files) > 0:

        file0 = files[0]
        file, rest = file0.split('__')

        if file[1] == 'e':
            algo0, name0, n0, k0, d0, rep0 = file.split('_')
            cz = 1
        else:
            algo0, name0, n0, k0, rep0 = file.split('_')
            cz = 0

        ret = pd.DataFrame()
        df0 = pd.read_csv(file0)
        ret = pd.concat([ret, df0], ignore_index=True)
        i = 1
        v = False
        if len(files) > 1:
            v = True
            for i in range(1, len(files)):
                file1 = files[i]
                file, rest = file1.split('__')
                if cz == 1:
                    algo1, name1, n1, k1, d1, rep1 = file.split('_')
                    if n0 == n1 and k0 == k1 and d0 == d1:
                        df1 = pd.read_csv(file1)
                        ret = pd.concat([ret, df1], ignore_index=True)
                    else:
                        break
                else:
                    algo1, name1, n1, k1, rep1 = file.split('_')
                    if n0 == n1 and k0 == k1:
                        df1 = pd.read_csv(file1)
                        ret = pd.concat([ret, df1], ignore_index=True)
                    else:
                        break
        for j in range(i):
            os.remove(files[j])

        if cz == 1:
            out = algo0 + '_' + name0 + '_' + n0 + '_' + k0 + '_' + d0 + '__' + str(len(ret)) + '.csv'
        else:
            out = algo0 + '_' + name0 + '_' + n0 + '_' + k0 + '__' + str(len(ret)) + '.csv'
        if v:
            ret.to_csv('merge/' + out, sep=',', index=False)
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        files.remove('merge.py')
    return


merge()