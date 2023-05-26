
##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: November 7th 2022

#Import pandas for reading and analyzing CSV data:
import pandas as pd


csvFile = pd.read_csv("movie_locations.csv")
numHoods = input("order of most popular neighborhoods in movies:")
print(csvFile["Neighborhood"].value_counts()[:int(numHoods)])
numDirectors = input("order of most popular neighborhoods in movies:")
print(csvFile["Director/Filmmaker Name"].value_counts()[:int(numDirectors)])
