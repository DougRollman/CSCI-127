##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: November 1st 2022

import matplotlib.pyplot as plt
import pandas as pd


total = 0

pop = pd.read_csv("country_internet.csv")
grouped_data = pop.groupby("Continental region")
print("Continental region")
print(grouped_data["Continental region"], grouped_data["NO. OF Internet Plans"].mean())
region = input("choose a region:")
regionData = pop.groupby("Continental region").get_group(region)

for i in regionData["Country"]:
    total += 1

print("In region:", region)
print("number of countries:", total )
print("maximum number of internet plans:", regionData["NO. OF Internet Plans"].max())
print("minimum number of internet plans:", regionData["NO. OF Internet Plans"].min())

fileName = input("Please enter output file name: ")

grouped_data.get_group(region).plot.bar("Country","NO. OF Internet Plans")

plt.gcf().subplots_adjust(bottom=0.25)
    #so that the country name is displayed in full
plt.xlabel("Country in " + region)
    #The parameter in xlabel should be "Country in ...", where ... is the name of chosen region. The region name should be exactly the same as the corresponding region the csv file.
plt.ylabel("NO. OF Internet Plans")

#plt.show()
fig = plt.gcf()
fig.savefig(fileName)


