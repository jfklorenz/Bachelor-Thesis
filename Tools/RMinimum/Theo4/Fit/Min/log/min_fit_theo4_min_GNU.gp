#!/usr/bin/gnuplot
# ================================================
#	Fit : RMinimum - Theorem 4 - Minimum
# ================================================
#	General
set datafile separator ",";

#	Beschriftung
#set title 'Fit : f(n) = a * eps^(-1) * log2log2(n) + b' font ",18"
set key autotitle columnhead
set xlabel 'n' font ",18"
set ylabel 'f_{min}' font ",18"
set key left top

#	Ranges
set xrange[64:1048576]
set yrange[5.8:11]

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
a=1; b=0.001

#	Fitting Function: a * loglog(x)
f(x) = a * (0.5**(-1)) * log(x) / log(2) + b
fit f(x) "min_fit_theo4_min.csv" u 4:3 via a,b

# ================================================
#	Plot
set logscale x 2
ti = sprintf("Fit_{min}(n) = %.2f * 2 * log2(n) + %.2f", a, b)
plot "min_fit_theo4_min.csv" using 4:3 with lines ls 2, \
	f(x) t ti with lines ls 1

# ================================================
#	Output
set term png size 800,800;
set output 'min_fit_theo4_min.png'

# ================================================
