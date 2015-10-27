import matplotlib.pyplot as plt

# plot figure and show in window
def plot_mandelbrot(mandelbrot,xmin,xmax,ymin,ymax):
    plt.imshow(mandelbrot);
    plt.axis((xmin,xmax,ymin,ymax));

# plot figure and save to file
def save_mandelbrot(mandelbrot,xmin,xmax,ymin,ymax,iteration):
    plt.imshow(mandelbrot);
    plt.axis((xmin,xmax,ymin,ymax));
    filename = 'Mandelbrot' + iteration;
    savefig(filename+'.eps');
