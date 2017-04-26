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