import pyescher as pe
from scipy.special import jn, hankel1
import numpy as np

x = np.linspace(0, 20, 1000)
y1 = jn(1, x)
y2 = hankel1(2, x)

l1 = pe.Line(x,y1,label='Bessel function of the first kind of order 1')
l2 = pe.Line(x,y2,label='Hankel function of the first kind of order 2')
pe.plot_lines(l1,l2, 
              xlabel='x', 
              ylabel='y', 
              title='Bessel and Hankel functions',
              show_marker=True,
              nmarkers=21,
              cycle_markers=True,
              cycle_linestyle=True,
              marker_size=5,
              filename='assets/bessel_hankel_plot.png')