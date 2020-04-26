set terminal postscript eps enhanced color "Helvetica" 20

set key top left
set autoscale
set title "heptane ST Phi = 1.0"
set output "./output.eps"
set logscale y
set ylabel "ID (ms)"
set xlabel "1000/T (K^-1)"
#set xrange [0.3 to 1.5]
#set yrange [0.1 to 200]

#########################
# Replace with tag-name #
#########################

plot "IgniDelTimesCHmax.dout" using 2:3 with l dt 2 lw 1 lc "red" title "phi = 1.0, 1 bar",\
"exp_data.csv" using 1:2 with p pt 2 ps 1 lc "red" title "phi = 1.0, 1 bar"
