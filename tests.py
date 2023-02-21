from datetime import datetime, timedelta
from TLETool_new import Componants

tle = Componants(fp="txt_files/Just_ONE_TLE_2.txt")
epoch = float(tle.epoch)
print(epoch)

epoch_datetime = datetime(1960, 1, 10, 12, 0, 0) + timedelta(days=epoch)

date_str = epoch_datetime.strftime('%d-%m-%Y %H:%M:%S')
print(epoch_datetime)
print(date_str)
