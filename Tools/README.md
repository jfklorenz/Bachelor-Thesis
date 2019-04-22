# Tools
This folder contains all the code snippets used during the entire process.

The tools can be separated into three different groups, i.e. code used for both algorithms and code only used for one specific algorithm.

## Merge
This folder contains the file `merge.py`. It is used to merge multiple *.csv* data files of the same case.

For example, if the folder contains the files
`min_algo_16_64_200.csv`, `min_algo_16_64_400.csv`, `med_filter_16_64_3_110.csv` and `med_filter_16_64_3_310.csv`,
it will delete the files and produce new files named
`min_algo_16_64_600.csv` and `med_filter_16_64_3_420.csv`,
containing all the data from the previously removed files.

This works for both algorithms.

## RMinimum
This folder contains all files to produce the graphics used in the Thesis and also finding a fit with Gnuplot for the RMinimum algorithm.

Note: There exists one tool each for *fix n, variable k* and *variable k, fix n*, respectively.

## RMedian
This folder contains all files to produce the graphics used in the Thesis and also finding a fit with Gnuplot for the RMedian algorithm.
