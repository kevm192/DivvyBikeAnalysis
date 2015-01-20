
import pandas as pd
import numpy as np



def parse_date(date0):
   
    #return str(date0)[4:8]
    return str(date0)


def calc_distance(lat1,lon1,lat2,lon2):
    
    from math import sin, radians, cos, sqrt, atan2
    
    lon1, lat1, lon2, lat2 = map(radians, [float(lon1), float(lat1), float(lon2), float(lat2)])
    
    R = 6373
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
    c = 2 * atan2( sqrt(a), sqrt(1-a) )
    d = R * c #(where R is the radius of the Earth) 
    return d




def calcEstimatedPrecipitation(dfB,dfW):

    # Param: dfB - The bike dataset
    # Param: dfW - The NOAA weather dataset
    # Return: Precipitation array

    # The goal here is to calculate the estimated precipitation for each trip. This is accomplished by finding the maxing precipation column
    # from the weather dataset for the given day and station. The day is provided from the trip data and the closest weather station is in new_bike_data.csv
    prcp = np.zeros(len(dfB),'int64')
    for i,t in enumerate(dfB.iterrows()):
        #print t[1]['from_station_name']
       # weather_station = dfBS[dfBS['name'] == t[1]['from_station_name']]['Weather_Station'].values[0] 
        #print weather_station
            filt = np.empty(0)
            dist2 = dict_list[t[1]['from_station_name']].copy()
            while(len(filt) == 0):
                key = min(dist2, key=dist2.get)
                dist2.pop(key)
                is_weather_station = dfW['STATION_NAME'] == key
                is_date = dfW['DATE'] == t[1]['starttime']
                filt = dfW[is_weather_station & is_date]
            #print t[1]['starttime']    

            prcp[i] = filt['PRCP'].values[0]
            #dfW[is_weather_station]
            if i%1000 == 0: print i

### Main Function ###

# Load Datasets
dfBS = pd.read_csv('/Users/kevm1892/Documents/new_bike_data.csv')
dfB = pd.read_csv('/Users/kevm1892/Downloads/Divvy_Stations_Trips_2013/Divvy_Trips_2013.csv')
dfB0 = dfB.copy()
dfW = pd.read_csv('/Users/kevm1892/Documents/new_weather_data.csv')
dfW0 = dfW.copy()

dfW['DATE'] = dfW['DATE'].apply(parse_date) 

prcp = calcEstimatedPrecipitation(dfB,dfW)
