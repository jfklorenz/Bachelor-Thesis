#!/usr/bin/gnuplot
# ================================================
#	Fit : f(x) = 1 / (a * k**0.5)
# ================================================
#	General
set datafile separator ",";

#	Beschriftung
#set title 'Fit : f(k) = a * log2(log2(x)) + b'
set key autotitle columnhead
set xlabel 'k' font ",18"
set ylabel '10^6 * Varianz' font ",18"
set key right bottom
set key font ",18"

#	Ranges
set xrange[4:1024]
set yrange[2:6.35]

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
a=2*10**(-6); b=0.001

#	Fitting Function: a * loglog(x)
f(x) = a * log(x) / log(2) + b
fit f(x) "min_filter_E_V_k_csv.csv" u ($4):((10**6)*$3) via a,b

# ================================================
#	Plot
ti = sprintf("Fit_V(n) = %.2f * 2 * log2(k) + %.2f", a, b)
plot "min_filter_E_V_k_csv.csv" using ($4):((10**6)*$3) with lines ls 2, \
	f(x) t ti with lines ls 1

# ================================================
#	Output
set term png size 800,600;
set output 'fit_filter_V_k.png'

# ================================================
