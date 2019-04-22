# RMinimum
This project conains the implementation of the **RMinimum** algorithm
presented in the Paper *Fragile complexity of some classic comparison based problems*.

Included is the algorithm itself and its phases, collected data and test cases.

### Directory Tree
The project uses the following directory tree:

| Folder | Content |
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
| *algo.py* | *RMinimum* Algorithm |
| *p0.py* | Base case of 3 people |
| *p1.py* | Phase 1 - Generate W, L |
| *p2.py* | Phase 2 - Generate filter through L |
| *p3.py* | Phase 3 - Use filter on W |
| *p4.py* | Phase 4 - Recurse or finish |

---
# Data
The folder *Data* contains the collected data as *.csv*-files.

 Each files contains the four columns **min**, **rem**, **fgc** and **work** containing the respective data. The number of rows corresponds to the amount of repetitions.

The filenames have the following syntax:

> filename = rmin_n_k_rep.csv

| Var | Usage |
| ------ | ------ |
| *algo* | Name of the algorithm |
| *n* | n=log2(n0), where n0 is the size of the input set X |
| *k* | Input value k(n) |
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

For each case a randomized test was implemented as well as some customized
tests. The customized tests are chosen to represent extreme scenarios within
the logic of the algorithm.

The folder contains the following files: &check;



| File | Rnd | Cst | Tested |
| ------ | ------ | ------ | ------ |
| *pytest_algo.py* | &check; | &check; | `return == min(X)`, `n/2 <= work(n) <= 2*n` |
| *pytest_p1.py* | &check; | &check; | `min(cnt) == max(cnt) == 1`, `len(W) == len(L) == n/2`, `min(X) in W` |
| *pytest_p2.py* | &check; | &check; | `len(L) == len(M) == n/k`, `max(cnt) == n/k `, `M[i] == min(L[i])` |
| *pytest_p3.py* | &check; | &check; |  `len(W) == n/k`, `cnt[M[i]] == k`, `min(cnt(W[i]) == max(cnt(W[i]) == 1` |
| *pytest_p4.py* | &check; | &check; | Recursive call, `min(W') == min(X)`, `max(cnt) = log2(len(W'))`, `sum(cnt) == len(W') - 1` |


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
| *jupyter_p4.py* | Results of Phase 4|
| *jupyter_case_eps.py* | Results for the input *(X, k)* with `k = n**eps` |
| *jupyter_case_eps_fix_eps.py* | Results for the input *(X, k)* with `k = n**eps` with varying values for *n* for one fix *eps*  |
| *jupyter_case_eps_fix_n.py* | Results for the input *(X, k)* with `k = n**eps` with varying values for *eps* for one fix *n* |
| *jupyter_case_loglog.py* | Results for the input *(X, k)* with `k = log2(n)/log2(log2(n))`  |
