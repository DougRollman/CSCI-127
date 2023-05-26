##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: November 1st 2022

import matplotlib.pyplot as plt
import pandas as pd

fileName = input("Enter output file name: ")
base = 0.00

pop = pd.read_csv("country_internet.csv")
for i in pop['Country']:
    pop["Percentage"] =(pop["Internet users"] /pop["Population"]) * 100
    if round(pop["Percentage"].max(),2) > base:
        base = round(pop["Percentage"].max(),2)
        highestPercent = i
pop.plot(x = "Country", y = "Percentage")
print("maximum percentage of all countries:", highestPercent, round(pop["Percentage"].max(),2))
#plt.show()

fig = plt.gcf()
fig.savefig(fileName)


#groupedCountry = pop.groupby('Country')
