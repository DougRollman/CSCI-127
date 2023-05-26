##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: October 25th 2022

#Libraries for plotting and data processing:
import matplotlib.pyplot as plt

import pandas as pd

file = input("Enter a csv file: ")
borough = input("Enter borough (Bronx, Brooklyn, Queens, Manhattan, Staten Island): ")
filesave = input("Enter output name: ")
pop = pd.read_csv(file)

#Compute the fraction of the population in the Borough, and save as new column:
pop['Date of Interest'] = pop['date_of_interest']
pop['Fraction'] = pop[borough]/pop['case_count']

#Create a plot of date of interest versus fraction of pop. (with labels):
pop.plot(x = 'Date of Interest', y = 'Fraction')




print("Min: ", pop[borough].min())
print("Max: ", pop[borough].max())
print("Mean: ", round(pop[borough].mean(),3))
print("Median: ", pop[borough].median())
print("Standard Deviation: ",round(pop[borough].std(),3))

#Save to the file the user input in variable output
plt.show()
fig = plt.gcf()
fig.savefig(filesave)
