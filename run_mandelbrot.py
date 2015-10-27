from compute_mandelbrot import *
from plot_mandelbrot import *

xmin,xmax      = -2,1
ymin,ymax      = -1,1
resolution     = 2000
max_iterations = 50

mandelbrot = compute_mandelbrot(xmin,xmax,ymin,ymax,resolution,max_iterations)
plot_mandelbrot(mandelbrot,xmin,xmax,ymin,ymax)

#for iteration in range(max_iterations):
#  mandelbrot = compute_mandelbrot(xmin,xmax,ymin,ymax,resolution,iteration)
#  save_mandelbrot(mandelbrot,xmin,xmax,ymin,ymax,iteration)
