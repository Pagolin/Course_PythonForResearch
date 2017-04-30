import pandas as pd
import matplotlib.pyplot as plt

"""
Bird_data of previous lesson are further explored here using
pandas groupedby() method
"""

bird_data = pd.read_csv("./bird_data/bird_tracking.csv")

# Group bird_data by name
grouped_birds = bird_data.groupby("bird_name")

# mean() is preformed groupwise
mean_speeds = grouped_birds.speed_2d.mean()
mean_altitudes = grouped_birds.altitude.mean()

# Conversion of timestamps to dati_time format using pd.to_date() and save
# only the days of observation in a new column (as done "by hand" in the
# prev. lesson)
bird_data.date_time = pd.to_datetime(bird_data.date_time)
bird_data["date"] = bird_data.date_time.dt.date

#Examples of groupby() usage
grouped_bydates = bird_data.groupby("date")
mean_altitudes_perday = grouped_bydates.altitude.mean()

grouped_birdday = bird_data.groupby(["bird_name", "date"])
mean_altitudes_perday = grouped_birdday.altitude.mean()

#Get and plot mean daily speeds for the three birds

all_means = pd.Series(grouped_birdday["speed_2d"].mean())
eric_daily_speed  = all_means["Eric"]
sanne_daily_speed = all_means["Sanne"]
nico_daily_speed  = all_means["Nico"]

plt.figure(figsize=(10,10))
eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.title("Daily mean speed")
plt.xlabel("Day")
plt.ylabel("Mean speed (m/s)")
plt.savefig("./bird_plots/Mean_speed_all.pdf")

