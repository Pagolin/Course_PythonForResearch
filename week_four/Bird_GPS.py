import pandas as pd

bird_data = pd.read_csv("./bird_data/bird_tracking.csv")
print(bird_data.info())