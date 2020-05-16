#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Nicholas Holfester
Code gets data about New York State Weather Stations
- can be modified for other states

Code made using NOAA API, documentation available on the official NOAA website
"""
import requests
import pandas as pd
import matplotlib.pyplot as plt

# get NY stations
def fetch_state_stations(base_url, locationid, token):
    url = base_url+'stations'
    params = {'locationid': str(locationid)}
    
    r = requests.get(url, params = params, headers = token)
    
    data = r.json()['results']
    data_df = pd.DataFrame.from_dict(data)
    data_df.plot(x='longitude', y='latitude', kind='scatter', grid= True)
    plt.savefig('static/ny_stations.png')

    return data_df

def group_stations_ny(station_data):
    ny_dict = {}
    
    ny_dict['nyc'] = station_data[station_data['latitude'] < 41.5]
    ny_dict['western_up'] = station_data[station_data['longitude'] < -77]
    ny_dict['eastern_up'] = station_data[(station_data['latitude'] > 41.5) &\
            (station_data['longitude'] > -75)]
    ny_dict['north_ny'] = station_data[station_data['latitude'] > 43.5]
    
    return ny_dict

# already include station, date, etc
def get_temp(ny_dict, params, token):
    base_url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'
    params['datatypeid'] = 'DPNP' #TAVG
    
    # choose year range, 2015 to present will give decent sample size for viewing
    base_year = 2015
    year_range = range(2020-2015)
    # index through all years in range
    for i in year_range:
        year = str(base_year + i)
        params['startdate'] = year+'01-01'
        params['enddate'] = year+'12-31'
        
        # iterate though each region to get station-id's
        for key in ny_dict:
            region_ids = ny_dict[key]['id']
            
            # iterate though each station to get temperature information
            for j in range(len(region_ids.rows)):
                params['stationid'] = str(region_ids.iloc[j])
                
                r = requests.get(base_url, params=params, header=token)
                print(r)
                temp_df = pd.DataFrame.from_dict(r.json())
            
        return temp_df



# token dictionary
mytoken = "YoiLDWrDxUoZFonrlVYOrItiGgDiueBe"
token ={'token':mytoken}

# base url
base_url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'

# base parameters
datasetid = "GHCND"
datatypeid = ""             # temperature data code
limit = "1000"                  # amount of data max
stationid = "GHCND:USW00023129" # choose specific station, could do multiple
startdate = ""
enddate = ""
params = {'datasetid':datasetid, 'datatypeid':datatypeid, 'limit':limit, 'stationid':stationid,\
          'startdate':startdate, 'enddate':enddate}

# call functions
station_data_ny = fetch_state_stations(base_url, 'FIPS:36', token)
ny_dict = group_stations_ny(station_data_ny)

## testing temp get
j = 1
region_ids = ny_dict['nyc']['id']
params['stationid'] = str(region_ids.iloc[j])
params['startdate'] = '2012-01-01'
params['enddate'] = '2012-12-31'
params['datatypeid'] = 'TAVG'

url = base_url+'data'

r = requests.get(url, params = params, headers = token)
print(r)
data = r.json()


    
    
    











