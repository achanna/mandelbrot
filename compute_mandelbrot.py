import numpy

# return matrix of complex zeros, ie 0+0i
def initialize_complex_zeroes(resolution):
  return complex_zeroes

# return matrix of x and y coordinates in a complex plane, ie x+yi
def initialize_complex_coords(xmin,xmax,ymin,ymax,resolution):
    resolution = 1    #define resolution of matrix
    x = numpy.linspace(xmin, xmax, resolution) #establishes x array
    y = numpy.linspace(ymin, ymax, resolution) #establishes y array
    xv, yv = meshgrid(x, y) #creates meshgrid of x and y arrays
    complex_coords = xv+yx*i #define the function to plot from meshgrid
  return complex_coords

# initialize starting mandelbrot matrix, with each entry equal to max_iterations
def initialize_mandelbrot(resolution,max_iterations):
  return mandelbrot

# return matrix of true/false values, indicating where mandelbrot entries are equal to max_iterations
def compute_mask(mandelbrot,max_iterations):
  return mask

# evaluate fractal equation for each entry in mask, z = z^2+c
# using mask can dramatically speed up process
def evaluate_eqn(complex_zeroes,complex_coords,mask):
  return complex_zeroes

def compute_mandelbrot(xmin,xmax,ymin,ymax,resolution,max_iterations):
  complex_zeroes = initialize_complex_zeroes(resolution)
  complex_coords = initialize_complex_coords(xmin,xmax,ymin,ymax,resolution)
  mandelbrot     = initialize_mandelbrot(resolution,max_iterations)
  for iteration in range(max_iterations):
    mask = compute_mask(mandelbrot,max_iterations)
    complex_zeroes = evaluate_eqn(complex_zeroes,complex_coords,mask)
    mandelbrot[mask & (numpy.abs(complex_zeroes) > 2)] = iteration
  return mandelbrot
