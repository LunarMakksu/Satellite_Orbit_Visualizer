from TLETool_new import Componants
#from mpl_toolkits.basemap import Basemap
#from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from pyorbital.orbital import Orbital
from datetime import datetime, date

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()
print(today, ' | ', current_time)

filepath= "txt_files/Just_ONE_TLE_2.txt"
tle = Componants(fp=filepath)

satellite_name = str(tle.line0_TLE)
line1_TLE = tle.line1_TLE
line2_TLE = tle.line2_TLE

orb = Orbital(satellite_name, line1=line1_TLE, line2=line2_TLE)

times_range = np.arange(0, datetime.utcnow().hour, 0.01)
times_rad = np.arange(0, 2*np.pi, 0.01)


lon_list = []
lat_list = []
alt_list = []

for val in times_range:

    lon, lat, alt = orb.get_lonlatalt(val)
    lon_list.append(lon)
    lat_list.append(lat)
    alt_list.append(alt)

print(lon_list)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(lon_list, lat_list, alt_list)
ax.set_xlabel('Longitude (deg)')
ax.set_ylabel('Latitude (deg)')
ax.set_zlabel('Altitude (km)')
plt.show()
