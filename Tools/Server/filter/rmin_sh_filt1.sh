#!/bin/bash
#SBATCH --partition=general1
#SBATCH --nodes=1
#SBATCH --ntasks=40
#SBATCH --cpus-per-task=1
#SBATCH --mem=600000
#SBATCH --time=04:00:00

export OMP_NUM_THREADS=1
export PYTHONHOME=/home/memhierarchy/lorenz/venv
export PYTHONPATH=/home/memhierarchy/lorenz/venv/python

# Run 10 times.
/home/memhierarchy/lorenz/venv/bin/python rmin_filt1.py >& 01.out &
/home/memhierarchy/lorenz/venv/bin/python rmin_filt1.py >& 01.out &
/home/memhierarchy/lorenz/venv/bin/python rmin_filt1.py >& 01.out &
/home/memhierarchy/lorenz/venv/bin/python rmin_filt1.py >& 01.out &
/home/memhierarchy/lorenz/venv/bin/python rmin_filt1.py >& 01.out &
/home/memhierarchy/lorenz/venv/bin/python rmin_filt1.py >& 01.out &
/home/memhierarchy/lorenz/venv/bin/python rmin_filt1.py >& 01.out &
/home/memhierarchy/lorenz/venv/bin/python rmin_filt1.py >& 01.out &
/home/memhierarchy/lorenz/venv/bin/python rmin_filt1.py >& 01.out &
/home/memhierarchy/lorenz/venv/bin/python rmin_filt1.py >& 01.out &

# Wait for all child processes to terminate.
wait