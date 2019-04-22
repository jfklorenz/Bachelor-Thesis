#!/usr/bin/gnuplot
# ================================================
#	Fit : f(x) = 1 / (a * k**0.5)
# ================================================
#	General
set datafile separator ",";

#	Beschriftung
#set title 'Fit : f(k) = a / (k**0.5) + b' font ",18"
set key autotitle columnhead
set xlabel 'n' font ",18"
set ylabel 'V(n)' font ",18"
set key left top


#	Ranges
set xrange[512:1048576]
set yrange[0:0.0008]


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
a=0.4; b=0.0000001

#	Fitting Function: f(n) = a / n + b
f(x) = a / x + b
fit f(x) "min_filter_fit_E_V_n_csv.csv" u 3:2 via a,b

# ================================================
#	Plot
set logscale x 2
ti = sprintf("F(n) = %.2f / n +  %.2f", a, b)
plot "min_filter_fit_E_V_n_csv.csv" using 3:2 with lines ls 2, \
	f(x) t ti with lines ls 1

# ================================================
#	Output
set term png size 800,800;
set output 'min_filter_fit_E_n.png'

# ================================================
