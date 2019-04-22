# RMedian
This project conains the implementation of the **RMedian** algorithm
presented in the Paper *Fragile complexity of some classic comparison based problems*.

Included is the algorithm itself and its phases, collected data and test cases.

### Directory Tree
The project uses the following directory tree:

| Folder | Contains |
| ------ | ------ |
| *Algo* | Executable for the algorithm and phases |
| *Data* | Collected data from the algorithm saved as *.csv* files |
| *Test* | Unittests with PyTest and Jupyter |

---
# Folder: Algo
The folder *Algo* contains the following all the executables for
the algorithm and the separat phases.

The code can be run via:

`python filename.py`

The folder contains the following files:

| File | Usage |
| ------ | ------ |
| *algo.py* | *RMedian* Algorithm |
| *p1.py* | Phase 1 - Generating Buckets L, C, R |
| *p2.py* | Phase 2 - Filter Elements |
| *p3.py* | Phase 3 - Abort, recursive call, end |

---
# Data
The folder *Data* contains the collected data as *.csv*-files.

 Each files contains the four columns **min**, **rem**, **fgc** and **work** containing the respective data. The number of rows corresponds to the amount of repetitions.

The filenames have the following syntax:

> filename = rmed_n_k_d_rep.csv

| Var | Usage |
| ------ | ------ |
| *algo* | Name of the algorithm |
| *n* | n=log2(n0), where n0 is the size of the input set X |
| *k* | Input value k(n) |
| *d* | Input value d(n) |
| *rep* | Number of repetitions for the given case |

The folder also contains the file *data.py*, which prints a overview of all
the relevant cases for this project.

---
# Test

The folder *Test* contains the two subfolders *PyTest* and *Jupyter*.

The folder *PyTest* contains the unittests for this project. There are
randomized as well as customized test cases.

The folder *Jupyter* contains more generic cases to test the fragile
complexity of the algorithm.


## PyTest
This folder *PyTest* contains the unittests for the algorithm itself as
well as each phase respectively.

Randomized tast cases where implemented whenever possible, but especially
 phase 2 needs a very specific input, which is hard to implement a
randomized generator for. Therefor only manual cases for phase 2 exist.

The folder contains the following files: &check;


| File | Rnd | Cst | Tested |
| ------ | ------ | ------ | ------ |
| *pytest_algo.py* | &check; | &check; | Median was indeed found |
| *pytest_p1.py* | &check; | &check; | `|L| == |R|`, `||L|| == ||R||`, `|L| + |C| + |R| = k` |
| *pytest_p2.py* | &check; | &check; | `median in C`, `f_{med}(n) <= |L| + |R|` |
| *pytest_p3.py* | &check; | &check; | Correct selection of: abort, recursive call, end |


## Jupyter

The folder *Jupyter* contains in detail testcases for the algorithm and each
phase respectively.

At the top of each file the user can manually change the input of the
code below to generate and print out all relevant data.

| File | Usage |
| ------ | ------ |
| *jupyter_algo.py* | Explicit result of the algorithm |
| *jupyter_p1.py* | Results of Phase 1|
| *jupyter_p2.py* | Results of Phase 2|
| *jupyter_p3.py* | Results of Phase 3|
