##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: November 15th 2022



import pandas as pd
import folium

aftercare = pd.read_csv('after_school.csv')
print("Enter 1 for Borough/Community")
print("Enter 2 Grade Level / Age Group")
choice = input("Your choice: ")
if choice == "1":
    groupedData = aftercare.groupby("Borough/Community")
    borough = input("Enter Borough/Community name: ")
    boroughData = groupedData.get_group(borough)
    mapNYC = folium.Map(location=[40.75, -74.125],zoom_start=3)
    for index,row in boroughData.iterrows():
        lat = row["Latitude"]
        lon = row["Longitude"]
        name = row["Name"]
        newMarker = folium.Marker([lat, lon], popup=name)
        newMarker.add_to(mapNYC)
        #print(name)
    outFile = borough.lower()
    outFile = outFile.replace(" ", "_")
    outFile = outFile.replace("/", "_")
    mapNYC.save(outfile=outFile + "_after_school.html")
    #print(outFile + "_after_school")
elif choice == "2":
    age = input("Enter Grade Level / Age Group name: ")
    groupedData = aftercare.groupby("Grade Level / Age Group")
    ageData = groupedData.get_group(age)
    mapNYC = folium.Map(location=[40.75, -74.125],zoom_start=3)
    for index,row in ageData.iterrows():
        lat = row["Latitude"]
        lon = row["Longitude"]
        name = row["Name"]
        newMarker = folium.Marker([lat, lon], popup=name)
        newMarker.add_to(mapNYC)
        #print(name)
    outFile = age.lower()
    outFile = outFile.replace(" ", "_")
    outFile = outFile.replace("/", "_")
    #print(outFile + "_after_school")
    mapNYC.save(outfile=outFile + "_after_school.html")
        





