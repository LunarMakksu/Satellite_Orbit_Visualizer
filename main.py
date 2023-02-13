#thank the lord for chatgpt
#uses my TLETool

from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv
from datetime import date, time, datetime
from TLETool_new import Componants

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()
print(today, ' | ', current_time)

filepath = "Just_ONE_TLE.txt"
def extractTLE():
    with open ("Phoenix_TLEs.txt") as fp:
        lines = fp.readlines()
        #need lines 1753-1755
        n = 0
        min = 1752
        with open (f"./{filepath}", 'r+') as nf: #R/W
            while n<3:
                nf.write(lines[min])  # EXTRACTS LATEST TLE SET FROM FILE
                min += 1
                n += 1
        nf.close()
    fp.close()

 
with open ("Just_ONE_TLE.txt", 'r') as file:
    lines_TLE = file.readlines()
    file.close()

line1 = lines_TLE[1]
line2 = lines_TLE[2]

tle = Componants(fp=filepath)
satellite = twoline2rv(line1, line2, wgs72)
position, velocity = satellite.propagate(0, now.second, )
#print(position, ' | ', velocity)
print(tle.launch_year)