##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: November 15th 2022

import folium
import pandas as pd

hospitals = pd.read_csv('nyc_hospitals.csv')
outFile = input("Enter output file:")
#print(hospitals["Facility Name"])
mapNYC = folium.Map(location=[40.75, -74.125],zoom_start=3)

for index,row in hospitals.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Facility Name"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapNYC)

mapNYC.save(outfile=outFile)
