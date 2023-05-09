from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# generate the Earth sphere
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)

# generate the satellite orbit data
longitudes = np.radians([0, 45, 90, 135, 180, 225, 270, 315, 360])
latitudes = np.radians([0, 30, 60, 90, 60, 30, 0, -30, -60])
altitudes = np.array([42164, 42164, 42164, 42164, 42164, 42164, 42164, 42164, 42164])

# plot the Earth sphere
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='Blues')

# plot the satellite orbit
x_orbit = (altitudes + 6371) * np.cos(latitudes) * np.cos(longitudes)
y_orbit = (altitudes + 6371) * np.cos(latitudes) * np.sin(longitudes)
z_orbit = (altitudes + 6371) * np.sin(latitudes)
ax.plot(x_orbit, y_orbit, z_orbit, color='red', linewidth=2)

# set the axis limits and labels
ax.set_xlim(-70000, 70000)
ax.set_ylim(-70000, 70000)
ax.set_zlim(-70000, 70000)
ax.set_xlabel('X (km)')
ax.set_ylabel('Y (km)')
ax.set_zlabel('Z (km)')

plt.show()
