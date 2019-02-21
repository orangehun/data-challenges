import pandas as pd
import json

args = json.load(open('data.json','r'))
span = pd.read_csv("data_sources/hotels_data/agg.csv")

lowlat = span['lat'][0]
highlat = span['lat'][1]
lowlon = span['lon'][0]
highlon = span['lon'][1]

df = pd.read_csv(args['datafile'])[['lon','lat','name']]

unique = df.groupby("name").sum()
for i in range(len(unique)):
    unique['lat'][i] = unique['lat'][i] / 2
    unique['lon'][i] = unique['lon'][i] / 2
    
num = len(unique)

unique = unique.assign(Region_lat = np.zeros(shape = num)).assign(Region_lon = np.zeros(shape = num))

for row in range(num):
    
    for k in range(1, int(num / 100) + 1):
        if unique["lat"][row] <= (lowlat + k * (highlat - lowlat) / num * 100) and \
        unique["lat"][row] > (lowlat + (k - 1) * (highlat - lowlat) / num * 100):
            unique["Region_lat"][row] += k
            break
            
    for k in range(1, int(num / 100) + 1):
        if unique["lon"][row] <= (lowlon + k * (highlon - lowlon) / num * 100) and \
        unique["lon"][row] > (lowlon + (k - 1) * (highlon - lowlon) / num * 100):
            unique["Region_lon"][row] += k
            break
            
    if row % 100 == 0:
        print(row)

unique.to_csv(args['staging_folder'] + '/filtered.csv',index=None)