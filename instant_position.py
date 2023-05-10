import turtle
import time
from pyorbital.orbital import Orbital
from datetime import datetime
from TLETool_new import Componants
from get_latest_TLE import latest_TLE
import csv

filepath = "txt_files/Just_ONE_TLE.txt"
all_yes = ['yes',  'Y', 'y', 'YES', 'Yes']
y_n = input("Do you want to get the latest TLE? (Y/N) Bare in mind excessive downloads will result in a temp IP block.\n")
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

screen.bgpic("resources/map.gif")
    
screen.register_shape("resources/fp.gif")
ff = turtle.Turtle()
ff.shape("resources/fp.gif")
ff.shapesize(2,3,1)
ff.setheading(45)
ff.penup()

lat = float(lat)
lon = float(lon)

def direc(lon, lat):
    if lat >= 0:
        N_or_S_lat = 'N'
    else:
        N_or_S_lat = 'S'
    if lon >= 0:
        E_or_W_lon = 'E'
    else:
        E_or_W_lon = 'W'
    return N_or_S_lat, E_or_W_lon

print(f"\nTLE used is from {tle.date_str}\n")

with open ("txt_files/lat&lons.csv", 'w') as log:
    fieldnames = ["longitudes", "lattitude", "time", "day", "month", "year"]
    csv_w = csv.writer(log, delimiter=',')
    csv_w.writerow(fieldnames)
    row = [lon, lat, datetime.utcnow(), tle.day, tle.month, tle.year]
    csv_w.writerow(f"{row}\n")
log.close()

def writedata(lon, lat):
    with open ("txt_files/lat&lons.csv", 'a') as log:
        csv_w = csv.writer(log, delimiter=',')
        row = [lon, lat, datetime.utcnow(), tle.day, tle.month, tle.year]
        csv_w.writerow(row)
    log.close()

N_or_S_lat, E_or_W_lon = direc(lon, lat)
print(f"Faraday-Phoenix is at lattitude: {round(lat, 3)} {N_or_S_lat} and longitude: {round(lon, 3)} {E_or_W_lon}")
ff.goto(lon, lat)
#writedata(lon, lat)

ff.pendown()

#counter = 0
while True:
    lon, lat, alt = orb.get_lonlatalt(datetime.utcnow())
    time.sleep(1)
    N_or_S_lat, E_or_W_lon = direc(lon, lat)
    print(f"Faraday-Phoenix is at lattitude: {round(lat, 3)} {N_or_S_lat} and longitude: {round(lon, 3)} {E_or_W_lon}")
    ff.goto(lon,lat)
    #writedata(lon, lat)
    
    #counter += 1
    #if counter == 10:
      #  print("Exitting loop...")
       # break

#turtle.exitonclick()