import csv
import pandas as pd

top_nationalities = {}

drivers_df = pd.read_csv("drivers.csv")
results = pd.read_csv("results.csv")

results['position'] = pd.to_numeric(results['position'], errors='coerce')
results = results.dropna(subset=["position"])

drivers_df['driverId'] = pd.to_numeric(drivers_df['driverId'], errors='coerce')
drivers_df = drivers_df.dropna(subset=["driverId"])

print(results['position'])
top_racers = results[results['position'] == 1.0]

for row in top_racers.itertuples():
    cur_driver = row[2]
    cur_driver = drivers_df.loc[drivers_df['driverId'] == cur_driver]
    cur_nationality = cur_driver['nationality']
    #print(cur_nationality)
    #if cur_driver['nationality'] in top_nationalities:
     #   top_nationalities[cur_driver['nationality']] += 1
    #else:
    #    top_nationalities[cur_driver['nationality']] = 1

top_nationalities = dict(sorted(top_nationalities.items(), key=lambda item:item[1], reverse=True))


print(top_racers)






