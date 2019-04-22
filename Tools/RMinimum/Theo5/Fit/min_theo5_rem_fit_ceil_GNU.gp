#!/usr/bin/gnuplot
# ================================================
#	Fit : RMinimum - Theorem 5 - Minimum - Floor
# ================================================
#	General
set datafile separator ",";

#	Beschriftung
#set title 'Fit : f(n) = a * eps^(-1) * log2log2(n) + b' font ",18"
set key autotitle columnhead
set xlabel 'n' font ",18"
set ylabel 'f_{rem}' font ",18"
set key left top

#	Ranges
set logscale x
set xrange[64:1048576]
set yrange[0:30]


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
a=6.5; b=-8.5

#	Fitting Function: f(n) = a * eps ** (-1) * loglog(n) + b
f(x) = a * (log(x)/log(2)) / (log( log(x)/log(2)) / log(2)) + b
fit f(x) "min_theo5_fit_ceil_csv.csv" u 4:6 via a,b

# ================================================
#	Plot
set logscale x 2
ti = sprintf("F(n) = %.2f * log2(n)/log2(log2(n)) +  %.2f", a, b)
plot "min_theo5_fit_ceil_csv.csv" using 4:6 with lines ls 2, \
	f(x) t ti with lines ls 1

# ================================================
#	Output
set term png size 800,800;

# ================================================
