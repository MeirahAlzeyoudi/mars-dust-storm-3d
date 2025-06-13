# The PYTHON Script of the Contour Map Represents the Heights of Dust Result

# Import Libraries
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from numpy import array
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
import matplotlib.font_manager as fm

# Sample Data (replace with actual coordinates and height values)
DATA = array([
    [0, 0, 5],
    [10, 0, 10],
    [5, 10, 15]
])

x = DATA[:, 0]
y = DATA[:, 1]
z = DATA[:, 2]

def plot_contour(x, y, z, resolution=50, contour_method='linear'):
    resolution_str = str(resolution) + 'j'
    X, Y = np.mgrid[min(x):max(x):complex(resolution), min(y):max(y):complex(resolution)]
    points = [[a, b] for a, b in zip(x, y)]
    Z = griddata(points, z, (X, Y), method=contour_method)
    return X, Y, Z

X, Y, Z = plot_contour(x, y, z)

with plt.style.context("classic"):
    fig, ax = plt.subplots(figsize=(15, 15))
    ax.scatter(x, y, color="black", linewidth=1, edgecolor="ivory", s=50)

    # Add labels
    ax.set_xlabel('Longitude')
    ax.set_xlim(0, 15)
    ax.set_ylabel('Latitude')
    ax.set_ylim(0, 15)
    ax.set_title('Contour Map of Dust Storm Heights')

    plt.contourf(X, Y, Z, cmap='hot')
    plt.colorbar(label='Height (km)')
    plt.show()
