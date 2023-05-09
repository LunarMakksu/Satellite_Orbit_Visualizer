import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.cbook import get_sample_data
from matplotlib.image import imread

# Use world image with shape (360 rows, 720 columns) 
pngfile = '/Users/maxbird/Documents/Python-Projects/OrbitTracker/Satellite_Orbit_Visualizer/resources/earth_nasa_day.png'
fn = get_sample_data(pngfile, asfileobj=False)
img = imread(fn)   # get array of color

# Some needed functions / constant
r = 5
pi = np.pi
cos = np.cos
sin = np.sin
sqrt = np.sqrt

# Prep values to match the image shape (360 rows, 720 columns)
phi, theta = np.mgrid[0:pi:360j, 0:2*pi:720j]

# Parametric eq for a spherical globe
# phi=latitude; theta=longitude
x = r * sin(phi) * cos(theta)
y = r * sin(phi) * sin(theta)
z = r * cos(phi)

fig = plt.figure()
fig.set_size_inches(9, 9)
ax = fig.add_subplot(111, projection='3d', label='axes1')

# drape the image on the globe's surface
sp = ax.plot_surface(x, y, z, \
                rstride=2, cstride=2, \
                facecolors=img)

# plot some points above/around the globe
phi, theta = np.mgrid[0:pi:50j, 0:2*pi:50j]
r2 = 1.5*r
x = r2 * sin(phi) * cos(theta)
y = r2 * sin(phi) * sin(theta)
z = r2 * cos(phi) + 0.8* sin(sqrt(x**2 + y**2)) * cos(2*theta)
ax.scatter(x, y, z, s=1, color='red')

ax.set_axis_off()
ax.set_aspect('auto')

plt.show()