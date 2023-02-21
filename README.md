# Satellite Orbit Estimator
Whilst I was completing some work experience at In Space Missions, I wanted to try develop a program that could propagate and visualize the orbit of their flagship spacecraft Faraday-Phoenix. This proved more difficult than I thought. This repo is my efforts to develop this software.
 
 
 # Instant Position
 ```console
 python instant_position.py
 ```
 
Background:
Program to retrieve latest [TLE](https://en.wikipedia.org/wiki/Two-line_element_set) and use my self-built [TLE tool](https://github.com/LunarMakksu/TLE_Tools) to split into its seperate elements. 
It then uses the PyOrbital library to calculate its longitude and lattitude, using UTC time, and set the turtle's position onto this on the map. The map will not update and will exit on click.

Usage:
Upon starting the program, the user will be prompted on weather they would like to retrieve the latest TLE from [Celestrak](https://celestrak.org/). **Please note**, fetching TLE information more than 5 times in 24 hours may cause your IP to be restricted by Celestrak (found this out the hard way), this will only be temporary. If not, program will use latest TLE stored in file **txt_files/Just_One_TLE.txt**. 

<img src="https://github.com/LunarMakksu/Satellite_Orbit_Visualizer/blob/main/resources/example.png" width = 900, length = 400>




**Current Bugs:**

-No while loop working to continously update instant position
-No complete orbit progragation 

# Future Development

End goal is to have a 2D or 3D plot of the satellites orbit with respect to the Earth's surface, with predictions of when it'll pass over your/a specified location. Would appreciate any help or guidance you can give me on proapagting orbits :)
