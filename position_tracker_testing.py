import turtle
import urllib.request
from pyorbital.orbital import Orbital
from pathlib import Path
from datetime import datetime
from TLETool_new import Componants

url ="https://celestrak.org/NORAD/elements/gp.php?CATNR=48924"
response = urllib.request.urlopen(url)
lines = response.readlines()
filepath = "txt_files/Just_ONE_TLE_2.txt"
path = Path(f'{filepath}')
print(path.is_file())

if path.is_file():
    with open (f"{filepath}", 'r+') as f:
        f.truncate(0)
        for line in lines:
            f.writelines(line.decode())
        f.close()

else:
    with open (f"./{filepath}", 'r+') as f:
        for line in lines:
            f.writelines(line.decode())
        lines_read = f.readlines()
        f.close()

tle = Componants(fp=filepath)

line0_TLE = tle.line0_TLE.rstrip('\n')
line1_TLE = tle.line1_TLE.rstrip('\n')
line2_TLE = tle.line2_TLE.rstrip('\n')
print(line0_TLE)
print(line1_TLE)

orb = Orbital(line0_TLE, line1=line1_TLE, line2=line2_TLE)
lon, lat, alt = orb.get_lonlatalt(datetime.utcnow())

screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# load the world map image
screen.bgpic("map.gif")
screen.register_shape("fp.gif")
ff = turtle.Turtle()
ff.shape("fp.gif")
ff.setheading(45)
ff.penup()

lat = float(lat)
lon = float(lon)

if lat >= 0:
    N_or_S_lat = 'N'
else:
    N_or_S_lat = 'S'
if lon >= 0:
    N_or_S_lon = 'E'
else:
    N_or_S_lon = 'W'

print(f"Faraday-Phoenix is at lattitude: {round(lat, 3)} {N_or_S_lat} and longitude: {round(lon, 3)} {N_or_S_lon}")
ff.goto(lon,lat)
turtle.exitonclick()