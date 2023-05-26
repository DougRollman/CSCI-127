##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
##Date: October 25th 2022

#Libraries for plotting and data processing:
import matplotlib.pyplot as plt

import pandas as pd

print("Enter a choice: ")
print("a. group by borough")
print("b. group by year")
choice = input()
children_lead = pd.read_csv('children_lead.csv.')

if choice == "a":
    print("average number of affected children by borough")
    print(children_lead.groupby('borough')['affected_children'].mean())
    boroughChoice = input("Enter a borough:")
    boroughGroup = children_lead.groupby('borough').get_group(boroughChoice)
    print("average number of affected children of", boroughChoice,"is", boroughGroup['affected_children'].mean())
    print("min number of affected children of", boroughChoice,"is",boroughGroup['affected_children'].min())
    print("max number of affected children of", boroughChoice, "is",boroughGroup['affected_children'].max())
elif choice == "b":
    print("average number of affected children by year")
    print(children_lead.groupby('year')['affected_children'].mean())
    yearChoice = input("Enter a year (2005 - 2016): ")
    yearGroup = children_lead.groupby('year').get_group(yearChoice)
    print("average number of affected children in", yearChoice, "is", yearGroup['affected_children'].mean())
    print("min number of affected children in", yearChoice, "is", yearGroup['affected_children'].min())
    print("max number of affected children in", yearChoice, "is", yearGroup['affected_children'].max()) 
    
else:
    print("wrong choice")




#pop['Date of Interest'] = pop['date_of_interest']
#pop['Fraction'] = pop[borough]/pop['case_count']

#Create a plot of date of interest versus fraction of pop. (with labels):
#pop.plot(x = 'Date of Interest', y = 'Fraction')




#print("Min: ", pop[borough].min())
#print("Max: ", pop[borough].max())
#print("Mean: ", round(pop[borough].mean(),3))
#print("Median: ", pop[borough].median())
#print("Standard Deviation: ",round(pop[borough].std(),3))

#Save to the file the user input in variable output
#plt.show()
#fig = plt.gcf()
#fig.savefig(filesave)
