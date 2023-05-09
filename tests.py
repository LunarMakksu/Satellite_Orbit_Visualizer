from datetime import datetime, timedelta
from TLETool_new import Componants

tle = Componants(fp="txt_files/Just_ONE_TLE.txt")

print(tle.mean_motion)
