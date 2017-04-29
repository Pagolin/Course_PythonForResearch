import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


bird_data = pd.read_csv("./bird_data/bird_tracking.csv")

#print(bird_data.info())

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

"""Work with timestamp data 
Timestamps are often (as in this case) given as strings. Pythons datetime libraray 
allows converting them into datetime objects
"""
import datetime
times_string = bird_data.date_time

timestamps = []
# datetimes function strptime(string, format_string) turns the first string argument into a datetime object, according to a format specified in it's second, format string argument

for k in range(len(bird_data)):
    timestamps.append(datetime.datetime.strptime(bird_data.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))
#print(timestamps[0:3])

# append the timestamps as a new column to bird_data
bird_data["timestamp"] = pd.Series(timestamps, index=bird_data.index)
#print(bird_data.head())

# Calculate elapsed time since the first observation for the data of Eric
eric_data = bird_data[bird_data.bird_name=="Eric"]
eric_times = eric_data.timestamp
elapsed_times = [time - eric_times[0] for time in eric_times]

# To get the times in a particular unit i.e. hours, days etc. divide timestamp object by a timedelta object
# As elapsed_times is a numpy array division is done elementwise without list comprehension

elapsed_days = np.array(elapsed_times)/datetime.timedelta(days=1)
print(elapsed_times[0:3])
print(elapsed_days[0:3])


"""Calculating mean daily speed -> Working with timestamps"""

next_day = 1
inds=[]
daily_mean_speed=[]
#Reminder enumerate returns (index, value) tuples
for (i, t) in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        daily_mean_speed.append(np.mean(eric_data.speed_2d[inds]))
        next_day += 1
        inds = []

plt.figure(figsize=(12,6))
plt.subplot(121)
plt.plot(elapsed_days)
plt.title("Days between observations")
plt.xlabel("Observation")
plt.ylabel("Elapsed time in days")
plt.subplot(122)
plt.plot(daily_mean_speed)
plt.title("Daily mean speed")
plt.xlabel("Day")
plt.ylabel("Mean speed (m/s)")
plt.savefig("./bird_plots/Speed_measures_Eric.pdf")

"""
Using Cartopy, a library with cartographic tools for python
In contrast to the flight plot before, the one, constructed here is not spacial distorted but maps to the speric 
ground, i.e. earth surface maps
"""

import cartopy.crs as ccrs
import cartopy.feature as cfeature

# One type of global map projection in cartopy is mercator
globe_map = ccrs.Mercator()
plt.figure(figsize=(10,10))
# Set the axes, extension and features of the map
axes = plt.axes(projection= globe_map)
axes.set_extent((-25.0, 20.0, 52.0, 10))
axes.add_feature(cfeature.LAND)
axes.add_feature(cfeature.OCEAN)
axes.add_feature(cfeature.COASTLINE)
axes.add_feature(cfeature.BORDERS, linestyle=':')

for name in bird_names:
    inds = bird_data['bird_name'] == name
    x,y = bird_data.longitude[inds], bird_data.latitude[inds]
    axes.plot(x, y,'.', transform=ccrs.Geodetic(), label=name )
plt.legend(loc="upper left")
plt.savefig("./bird_plots/flight_map.pdf")
#TODO: Solve troubly with cartopy url.
# Error:File "/home/lisza/Tools/anaconda3/lib/python3.6/urllib/request.py", line 1320, in do_open
#   raise URLError(err)
#urllib.error.URLError: <urlopen error [Errno -5] Zu diesem Hostnamen gehört keine Adresse>
