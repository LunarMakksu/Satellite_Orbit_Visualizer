from mpl_toolkits.basemap import Basemap
from pyorbital.orbital import Orbital
import matplotlib.pyplot as plt
import numpy as np
from datetime import time, datetime, timedelta
from PIL import Image
from get_latest_TLE import latest_TLE
from TLETool_new import Componants

all_d = ['d', 'D', 'day', 'Day']
all_n = ['n', 'N', 'night', 'Night']
all_yes = ['yes',  'Y', 'y', 'YES', 'Yes']
all_2d = ['2d', '2D', '2 d', '2 D', '2']
all_3d = ['3d', '3D', '3 d', '3 D', '3']


filepath = "txt_files/Just_ONE_TLE.txt"
y_n = input("Do you want to get the latest TLE? (Y/N) Bare in mind excessive downloads will result in a temp IP block.")
if y_n in all_yes:
    sure = input("Are you sure? Please confirm (Y/N)")
    if sure in all_yes:
        latest_TLE.get_latest_TLE(fp=filepath)
    else:
        print("Latest TLE not fetched")
        pass

tle = Componants(fp=filepath)
print(f"TLE is from {tle.date_str}")

plot_dimen = input("Do you want a 2D or 3D plot?")
if plot_dimen in all_2d:
    plot_d = 2
    dayornight = input("Would you like a day or night map? D = day, N = night")
    if dayornight in all_n:
        map = 'resources/earth_nasa_night.png'
    else:
        print("invalid input, map set to day by default")
        map = 'resources/earth_nasa_day.png'

elif plot_dimen in all_3d:
    plot_d = 3
else:
    print("Invalid input, 2D plot set by default")
    plot_d = 2

line0_TLE = tle.line0_TLE.rstrip('\n')
line1_TLE = tle.line1_TLE.rstrip('\n')
line2_TLE = tle.line2_TLE.rstrip('\n')

# Load the timescale and set the start and end times
#timescale = load.timescale()
start_time = datetime.utcnow()
end_time = start_time + timedelta(hours=6)

# Generate an array of times
times = np.arange(0, (end_time-start_time).total_seconds(), 10.0)

orb = Orbital(line0_TLE, line1=line1_TLE, line2=line2_TLE)
# Compute the latitude, longitude, and altitude of the satellite at each time
latitudes, longitudes, altitudes = [], [], []
print("Calculating...")

if plot_d == 2:
    for time in times:
        try:
            time_utc = start_time + timedelta(seconds=time)
            longitude, latitude, altitude = orb.get_lonlatalt(time_utc)
            #print(f"Lat: {latitude} Lon: {longitude} Alt: {altitude}")
            altitudes.append(altitude)  # convert meters to kilometers
            if latitude < -68.0 and latitude < 83.0: #not desired values
                pass
            else:
                latitudes.append(latitude)
                longitudes.append(longitude)
        except:
            print("Problem with calculation")


elif plot_d == 3:
        for time in times:
            try:
                time_utc = start_time + timedelta(seconds=time)
                longitude, latitude, altitude = orb.get_lonlatalt(time_utc)
                #print(f"Lat: {latitude} Lon: {longitude} Alt: {altitude}")
                altitudes.append(altitude)  # convert meters to kilometers
                latitudes.append(latitude)
                longitudes.append(longitude)
            except:
                print("Problem with calculation")


print(f"Long max: {max(longitudes)} Long min: {min(longitudes)} Lat max: {max(latitudes)} Lat min: {min(latitudes)}")
print(f"Alt max: {max(altitudes)} Alt min: {min(altitudes)}")

def plot2d():
    map_image = Image.open(f'{map}')
    fig, ax = plt.subplots(figsize=(16, 8))

    ax.imshow(map_image, extent=[-180, 180, -90, 90])
    ax.plot(longitudes, latitudes, color='red', linewidth=2, linestyle='dotted')
    ax.set_xlabel('Longitude (degrees)')
    ax.set_ylabel('Latitude (degrees)')
    ax.set_title(f'Satellite Trajectory for {line0_TLE}')

    plt.show()


def plot3d():
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim(-180, 180)
    ax.set_ylim(-180, 180)
    ax.set_zlim(min(altitudes), max(altitudes))
    ax.set_xlabel('Longitude (degrees)')
    ax.set_ylabel('Latitude (degrees)')
    ax.set_title(f'Satellite Trajectory for {line0_TLE}')

    ax.plot(longitudes, latitudes, altitudes, color='red', linewidth=2, linestyle='dotted')

    plt.show()

if plot_d == 3:
    plot3d()
else:
    plot2d()