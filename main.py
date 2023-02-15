#thank the lord for chatgpt
#uses my TLETool

from pyorbital.orbital import Orbital
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from TLETool_new import Componants
from datetime import datetime, date

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()
print(today, ' | ', current_time)

filepath = "Just_ONE_TLE.txt"
#image_fp = "map.png"
#pi = np.pi
#GM = 398600.4418
tle = Componants(fp=filepath)
 
line1_TLE =  tle.line1_TLE.rstrip('\n')
line2_TLE =  tle.line2_TLE

name = f"{str(tle.satellite_name)}"
orb = Orbital(name, line1=line1_TLE, line2=line2_TLE)
#earth = Image.open(f'{image_fp}')

times_rad = np.arange(0, 2*np.pi, 0.01)
#lon_now, lat_now, alt_now = orb.get_position(datetime.utcnow(), normalize=True)
lon, lat, alt = orb.get_lonlatalt(datetime.utcnow())
#day_seconds = 24*60*60
#period = day_seconds * 1/tle.mean_motion

# Inferred semi-major axis (in km)
#semi_major_axis = ((period/(2*pi))**2 * GM)**(1./3)

'''
fig = plt.figure()
m = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution=None, lat_0=52, lon_0=0.13)
m.bluemarble()

x, y = m(lon, lat)
m.plot(x, y, color='red', linewidth=2)
plt.title('Satellite Orbit')
plt.show()
'''

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#m = Basemap(projection='ortho',lat_0=0,lon_0=0,resolution='l')
#m.bluemarble()
ax.set_xlabel('Longitude (deg)')
ax.set_ylabel('Latitude (deg)')
ax.set_zlabel('Altitude (km)')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

Earth_radius = 6371 # km
max_radius = 0

max_radius = max(max_radius, Earth_radius)

# Coefficients in a0/c x**2 + a1/c y**2 + a2/c z**2 = 1 
coefs = (1, 1, 1)  

# Radii corresponding to the coefficients:
rx, ry, rz = [Earth_radius/np.sqrt(coef) for coef in coefs]
x = rx * np.outer(np.cos(u), np.sin(v))
y = ry * np.outer(np.sin(u), np.sin(v))
z = rz * np.outer(np.ones_like(u), np.cos(v))

    # Plot:
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')
lon, lat, alt = orb.get_lonlatalt(datetime.utcnow())
ax.plot(lon, lat, alt)
plt.show()