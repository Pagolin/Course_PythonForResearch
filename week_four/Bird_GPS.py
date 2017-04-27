import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


bird_data = pd.read_csv("./bird_data/bird_tracking.csv")

print(bird_data.info())

"""draw a first plot of longitude vs latitude of bird flights, not yet taking into account the distortions caused by the fact, the plot is 2D-> flat,  while flight coordinates are measured over a speric ground"""


Eric_index = bird_data.bird_name =="Eric"
x, y = bird_data.longitude[Eric_index], bird_data.latitude[Eric_index]
#distorted flight/ migration path of bird Eric




bird_names = pd.unique(bird_data.bird_name)
plt.figure(figsize=(7,7))
for name in bird_names:
    name_index = bird_data.bird_name ==name
    x, y = bird_data.longitude[name_index], bird_data.latitude[name_index]
    plt.plot(x, y, ".", label=name)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
#plt.show()
plt.savefig("./bird_plots/uncorrected_paths.pdf")

"""Work with speed data (column 'speed_2d') of the birds to exemplify the handling of NAN's in the data"""

speed = bird_data.speed_2d[Eric_index]
#pyplot can't handle NAN#s -> find them with numpy
np.isnan(speed).any()
#or how many
np.sum(np.isnan(speed))
#or true or false for all elements in speed
ind = np.isnan(speed)
#take ~ind => Komplement of ind vektor where NAN's in speed are False
complement = ~ind
plt.figure(figsize= (12,4))
plt.subplot(221)
plt.hist(speed[complement], bins=np.linspace(0, 30, 20), normed=True)
plt.xlabel("2D speed in m/s")
plt.ylabel("Frequency")
plt.subplot(222)
plt.hist(speed[complement], bins=np.linspace(0, 30, 20), normed=False)
plt.xlabel("2D speed in m/s")
plt.ylabel("Frequency non-normed")
plt.savefig("./bird_plots/speed_hist_Eric.pdf")

#pandas irgnores NAN's when plotting data

plt.figure()
bird_data.speed_2d.plot(kind='hist', range = [0,30])
plt.xlabel("2D speed in m/s")
plt.ylabel("Frequency")
plt.savefig("./bird_plots/pandas_hist_Eric.pdf")
