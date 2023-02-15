
import matplotlib.pyplot as plt
import numpy as np
from TLETool_new import Componants
from datetime import datetime, date

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()
print(today, ' | ', current_time)

plt.rcParams["figure.figsize"] = [15, 20]
plt.rcParams["figure.autolayout"] = True
im = plt.imread("map.gif")
fig, ax = plt.subplots()
im = ax.imshow(im, extent=[0, 300, 0, 300])
x = np.array(range(300))
ax.plot(x, x, ls='dotted', linewidth=2, color='red')
plt.show()