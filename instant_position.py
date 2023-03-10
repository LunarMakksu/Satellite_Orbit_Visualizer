import turtle
from pyorbital.orbital import Orbital
from datetime import datetime
from TLETool_new import Componants
from get_latest_TLE import latest_TLE


filepath = "txt_files/Just_ONE_TLE.txt"
all_yes = ['yes',  'Y', 'y', 'YES', 'Yes']
y_n = input("Do you want to get the latest TLE? (Y/N) Bare in mind excessive downloads will result in an IP block.\n")
if y_n in all_yes:
    sure = input("Are you sure? Please confirm (Y/N)")
    if sure in all_yes:
        latest_TLE.get_latest_TLE(fp=filepath)

tle = Componants(fp=filepath)

line0_TLE = tle.line0_TLE.rstrip('\n')
line1_TLE = tle.line1_TLE.rstrip('\n')
line2_TLE = tle.line2_TLE.rstrip('\n')

orb = Orbital(line0_TLE, line1=line1_TLE, line2=line2_TLE)
lon, lat, alt = orb.get_lonlatalt(datetime.utcnow())

screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# load the world map image
screen.bgpic("resources/map.gif")
screen.register_shape("resources/fp.gif")
ff = turtle.Turtle()
ff.shape("resources/fp.gif")
ff.setheading(45)
ff.penup()

lat = float(lat)
lon = float(lon)

if lat >= 0:
    N_or_S_lat = 'N'
else:
    N_or_S_lat = 'S'
if lon >= 0:
    E_or_W_lon = 'E'
else:
    E_or_W_lon = 'W'

print(f"\nTLE used is from {tle.date_str}\n")
print(f"Faraday-Phoenix is at lattitude: {round(lat, 3)} {N_or_S_lat} and longitude: {round(lon, 3)} {E_or_W_lon}")
ff.goto(lon,lat)
turtle.exitonclick()