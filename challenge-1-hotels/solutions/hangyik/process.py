# coding: utf-8

import pandas as pd
import numpy as np
import json

input_json = json.load(open('input.json','r'))
data_args = json.load(open('data.json','r'))
data = pd.read_csv(data_args['staging_folder'] + '/filtered.csv')

out = []

for place in input_json:
        
    cross = []
    r = 0
        
    while True:
            
        r += 10
        
        by_lat = data.loc[abs(data["lat"] - place["lat"]) <= r].reset_index(drop = True)
        by_lon = data.loc[abs(data["lon"] - place["lon"]) <= r].reset_index(drop = True)
        by_lat["distance"] = (place['lon'] - by_lat['lon']) ** 2 + (place['lat'] - by_lat['lat']) ** 2
        by_lon["distance"] = (place['lon'] - by_lon['lon']) ** 2 + (place['lat'] - by_lon['lat']) ** 2        
        lat_min = by_lat.loc[by_lat["distance"] == by_lat["distance"].min()].reset_index(drop = True)
        lon_min = by_lon.loc[by_lon["distance"] == by_lon["distance"].min()].reset_index(drop = True)
        
        if len(lat_min) == 0 or len(lon_min) == 0:
            continue        
        
        if lat_min["name"].values[0] == lon_min["name"].values[0]:
            closest_place = {'lon': lat_min['lon'].values[0], 'lat': lat_min['lat'].values[0],
                     'name': lat_min["name"].values[0]}
            out.append(closest_place.copy())
            break

json.dump(out,open('output.json','w'))