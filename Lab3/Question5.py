import numpy as np
from scipy.interpolate import CubicSpline, Akima1DInterpolator, BarycentricInterpolator
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# We can change the function at one place for ease of testing
def f(x):
    return np.tan(x)*np.sin(30*x)*np.exp(x)

# Number of sampling points for the interpolation: We can change it at one place for ease of testing
num_points = [i for i in range(2,36)]


interpolation_functions = [
                            CubicSpline
                           , Akima1DInterpolator
                           , BarycentricInterpolator
                           ]
interpolation_names = [
                        'Cubic Spline'
                       , 'Akima'
                       , 'Barycentric'
                       ]

interpolation_colors = [
                         'r'
                        , 'g'
                        , 'purple'
                        ]

# Set up the plot
fig, ax = plt.subplots()

# Update function used for the animation, here `frame` is the index of the number of time this was called
def update(frame):
    ax.clear()
    # ax.set_xlim(0, 1.0)
    ax.set_ylim(-4.0, 4.0)

    # number of points to sample in current iteration/call of the update fn
    num = num_points[frame]
    
    # Plot the true function, sampling 500 points so that curve looks smooth
    x = np.linspace(0, 1.0, 500)
    y = f(x)
    ax.plot(x, y, label='True')
    
    # Generate the data for the plot for the current iteration/call of the update fn
    x = np.linspace(0, 1.0, num)
    y = f(x)


    # Plot the different interpolation functions
    for i, fn in enumerate(interpolation_functions):
        f_int = fn(x, y)                                    # now f_int willbe interpolated function
        x1=np.linspace(0, 1.0, 500)                         # sampling 500 points so that curve looks smooth
        ax.plot(x1, f_int(x1), label=interpolation_names[i], c=interpolation_colors[i])

    # Add the legend, set graph title, labels, add grid
    ax.legend(loc='upper left')
    ax.set_title(r'Different interpolations for $tan(x) \cdot sin(30x) \cdot e^x$'+ ' for {} samples'.format(num))
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$f(x)$')
    ax.grid()


# Create the animation but keep a reference to it
anim = FuncAnimation(fig, update, frames=len(num_points), repeat=False)

# Show the animation
anim.save('./interpolations.gif', writer='imagemagick', fps=2)
plt.show()

s