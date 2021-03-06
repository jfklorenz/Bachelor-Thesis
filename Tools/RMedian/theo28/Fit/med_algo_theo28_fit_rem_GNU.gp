#!/usr/bin/gnuplot
# ================================================
#	Fit : RMedian - Theorem 28 - Remaining
# ================================================
#	General
set datafile separator ",";

#	Beschriftung
set key autotitle columnhead
set xlabel 'n' font ",18"
set ylabel 'f_{med}' font ",18"
set key left top

#	Ranges
set xrange[65536:262144]
set yrange[400:1100]


# ================================================
#	Style
set style line 1 \
    linecolor rgb '#0060ad' \
    linetype 1 linewidth 2 \
    pointtype 7 pointsize 1.5

set style line 2 \
    linecolor rgb '#dd181f' \
    linetype 1 linewidth 2 \
    pointtype 5 pointsize 0.5

# ================================================
#	Fit Parameters
FIT_LIMIT=1e-6;
a=0.25; b=0.01

#	Fitting Function:
f(x) = a * (x**(0.5)) + b
fit f(x) "med_algo_theo28_data.csv" u 2:4 via a,b

# ================================================
#	Plot
ti = sprintf("Fit(n) = %.2f * n^{1/2} +  %.2f", a, b)
plot "med_algo_theo28_data.csv" using 2:4 with lines ls 2, \
	f(x) t ti with lines ls 1

# ================================================
#	Output
set term png size 800,800;
set output 'med_algo_theo28_fit_rem.png'

# ================================================
