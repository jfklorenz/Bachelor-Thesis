#!/usr/bin/gnuplot
# ================================================
#	Fit : f(x) = 1 / (a * k**0.5)
# ================================================
#	General
set datafile separator ",";

#	Beschriftung
#set title 'Fit : f(k) = a / (k**0.5) + b' font ",18"
set key autotitle columnhead
set xlabel 'k' font ",18"
set ylabel 'µ' font ",18"
set key left top


#	Ranges
set xrange[4:1024]
set yrange[0:0.38]


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
a=0.6; b=0.003

#	Fitting Function: a * eps ** (-1) * loglog(x)
f(x) = a/sqrt(x) + b
fit f(x) "min_filter_E_V_k_csv.csv" u 4:2 via a,b

# ================================================
#	Plot
set logscale x 2
ti = sprintf("Fit(n) = %.2f / n**(1/2) +  %.2f", a, b)
plot "min_filter_E_V_k_csv.csv" using 4:2 with lines ls 2, \
	f(x) t ti with lines ls 1

# ================================================
#	Output
set term png size 800,800;
set output 'min_filter_fit_E_k.png'

# ================================================
